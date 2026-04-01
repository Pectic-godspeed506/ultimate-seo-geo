#!/usr/bin/env python3
"""
Unified crawl interface with pluggable backends.

Abstraction layer that other scripts use for fetching pages.
Supports requests (stdlib), firecrawl, and playwright backends.

Usage:
    python crawl_adapter.py https://example.com
    python crawl_adapter.py https://example.com --backend playwright
    python crawl_adapter.py https://example.com --json --timeout 20
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from typing import Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


USER_AGENT = (
    "Mozilla/5.0 (compatible; UltimateSEO/1.8; "
    "+https://github.com/mykpono/ultimate-seo-geo)"
)

DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}

_BACKENDS = ("requests", "firecrawl", "playwright")


@dataclass
class CrawlResult:
    url: str
    final_url: str = ""
    html: str = ""
    status_code: Optional[int] = None
    headers: dict = field(default_factory=dict)
    error: Optional[str] = None


def _detect_backend() -> str:
    if os.environ.get("FIRECRAWL_API_KEY"):
        return "firecrawl"
    return "requests"


def _fetch_requests(url: str, timeout: int = 15) -> CrawlResult:
    result = CrawlResult(url=url)
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
    if parsed.scheme and parsed.scheme not in ("http", "https"):
        result.error = f"Invalid URL scheme: {parsed.scheme}"
        return result

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = Request(url, headers=DEFAULT_HEADERS)
    try:
        resp = urlopen(req, timeout=timeout, context=ctx)
        result.status_code = resp.status
        result.final_url = resp.url
        result.headers = dict(resp.headers.items())
        raw = resp.read()
        charset = resp.headers.get_content_charset() or "utf-8"
        try:
            result.html = raw.decode(charset, errors="replace")
        except (LookupError, UnicodeDecodeError):
            result.html = raw.decode("utf-8", errors="replace")
    except HTTPError as e:
        result.status_code = e.code
        result.final_url = url
        result.headers = dict(e.headers.items()) if e.headers else {}
        try:
            result.html = e.read().decode("utf-8", errors="replace")
        except Exception:
            pass
    except URLError as e:
        result.error = f"Connection error: {e.reason}"
    except TimeoutError:
        result.error = f"Request timed out after {timeout}s"
    except Exception as e:
        result.error = f"Fetch failed: {e}"
    return result


def _fetch_firecrawl(url: str, timeout: int = 15) -> CrawlResult:
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        print(
            "Firecrawl backend selected but FIRECRAWL_API_KEY not set. "
            "Falling back to requests backend.",
            file=sys.stderr,
        )
        return _fetch_requests(url, timeout)

    try:
        from firecrawl import FirecrawlApp  # type: ignore
        app = FirecrawlApp(api_key=api_key)
        response = app.scrape_url(url)
        return CrawlResult(
            url=url,
            final_url=response.get("metadata", {}).get("url", url),
            html=response.get("html", response.get("content", "")),
            status_code=response.get("metadata", {}).get("statusCode", 200),
            headers=response.get("metadata", {}).get("headers", {}),
        )
    except ImportError:
        print(
            "Firecrawl SDK not installed. Install with: pip install firecrawl-py\n"
            "Or use the Firecrawl MCP server. Falling back to requests backend.",
            file=sys.stderr,
        )
        return _fetch_requests(url, timeout)
    except Exception as e:
        print(f"Firecrawl error: {e}. Falling back to requests backend.", file=sys.stderr)
        return _fetch_requests(url, timeout)


def _fetch_playwright(url: str, timeout: int = 15) -> CrawlResult:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        print(
            "Playwright not installed. Install with: pip install playwright && "
            "playwright install chromium\nFalling back to requests backend.",
            file=sys.stderr,
        )
        return _fetch_requests(url, timeout)

    result = CrawlResult(url=url)
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page(user_agent=USER_AGENT)
            resp = page.goto(url, timeout=timeout * 1000, wait_until="networkidle")
            if resp:
                result.status_code = resp.status
                result.headers = resp.all_headers()
            result.final_url = page.url
            result.html = page.content()
            browser.close()
    except Exception as e:
        result.error = f"Playwright error: {e}"
        if not result.html:
            fallback = _fetch_requests(url, timeout)
            if not fallback.error:
                return fallback
    return result


_BACKEND_MAP = {
    "requests": _fetch_requests,
    "firecrawl": _fetch_firecrawl,
    "playwright": _fetch_playwright,
}


class CrawlAdapter:
    """Unified crawl interface with pluggable backends."""

    def __init__(self, backend: str = "requests"):
        if backend == "auto":
            backend = _detect_backend()
        if backend not in _BACKENDS:
            raise ValueError(f"Unknown backend '{backend}'. Choose from: {_BACKENDS}")
        self.backend = backend
        self._fetch_fn = _BACKEND_MAP[backend]

    def fetch(self, url: str, timeout: int = 15) -> CrawlResult:
        return self._fetch_fn(url, timeout)

    def fetch_many(
        self, urls: list[str], max_workers: int = 5, timeout: int = 15
    ) -> list[CrawlResult]:
        results: list[CrawlResult] = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self._fetch_fn, url, timeout): url for url in urls
            }
            for future in as_completed(futures):
                results.append(future.result())
        return results

    def __repr__(self) -> str:
        return f"CrawlAdapter(backend={self.backend!r})"


def main():
    parser = argparse.ArgumentParser(
        description="Fetch a page using the unified crawl adapter"
    )
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument(
        "--backend", "-b",
        choices=["auto", *_BACKENDS],
        default="auto",
        help="Crawl backend (default: auto-detect)",
    )
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--timeout", "-t", type=int, default=15, help="Timeout in seconds (default: 15)"
    )
    args = parser.parse_args()

    adapter = CrawlAdapter(backend=args.backend)
    result = adapter.fetch(args.url, timeout=args.timeout)

    if args.json:
        print(json.dumps(asdict(result), indent=2, default=str))
        return

    if result.error:
        print(f"Error: {result.error}", file=sys.stderr)
        sys.exit(1)

    print(result.html)
    print(f"\nBackend: {adapter.backend}", file=sys.stderr)
    print(f"URL: {result.final_url}", file=sys.stderr)
    print(f"Status: {result.status_code}", file=sys.stderr)
    print(f"Size: {len(result.html)} bytes", file=sys.stderr)


if __name__ == "__main__":
    main()
