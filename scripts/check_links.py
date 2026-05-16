#!/usr/bin/env python3
"""Check Markdown links and the curated resources file.

The checker intentionally uses only the Python standard library so it can run in
GitHub Actions without installing dependencies.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import time
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    Path("README.md"),
    Path("START_HERE.md"),
    Path("Contributing.md"),
    Path("MAINTENANCE.md"),
    Path(".github/ISSUE_TEMPLATE/resource-suggestion.md"),
    Path(".github/ISSUE_TEMPLATE/stale-or-broken-link.md"),
    Path(".github/pull_request_template.md"),
]

BROWSER_ONLY_URLS = {
    "https://www.kaggle.com/learn",
    "https://portswigger.net/web-security",
    "https://stackoverflow.com/help/asking",
}

OK_HTTP_ERRORS = {401, 403, 429}

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)#][^)]*)\)")
RESOURCE_URL = re.compile(r"^\s+url:\s+(https?://\S+)\s*$", re.MULTILINE)


def iter_markdown_links(path: Path) -> Iterable[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    for match in MARKDOWN_LINK.finditer(text):
        url = match.group(1).strip()
        if not url.startswith(("http://", "https://")):
            local = (path.parent / url).resolve()
            try:
                local.relative_to(ROOT)
            except ValueError:
                yield url, f"{path}: local link escapes repository"
                continue
            if not local.exists():
                yield url, f"{path}: local file does not exist"
            continue
        line = text[: match.start()].count("\n") + 1
        yield url, f"{path}:{line}"


def iter_resource_urls(path: Path) -> Iterable[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    for match in RESOURCE_URL.finditer(text):
        line = text[: match.start()].count("\n") + 1
        yield match.group(1), f"{path}:{line}"


def check_url(url: str, timeout: int) -> tuple[bool, str]:
    context = ssl.create_default_context()
    headers = {
        "User-Agent": "Mozilla/5.0 link-check for ashleymcnamara/learn_to_code",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    for method in ("HEAD", "GET"):
        try:
            request = Request(url, method=method, headers=headers)
            with urlopen(request, timeout=timeout, context=context) as response:
                code = response.getcode()
                return 200 <= code < 400, str(code)
        except HTTPError as error:
            if method == "HEAD" and error.code in {403, 405, 406, 429}:
                continue
            if error.code in OK_HTTP_ERRORS:
                return True, f"HTTP {error.code}"
            return False, f"HTTP {error.code}"
        except (TimeoutError, URLError, OSError) as error:
            if method == "HEAD":
                continue
            return False, f"{type(error).__name__}: {error}"

    return False, "unknown error"


def collect_urls(include_resources: bool) -> dict[str, list[str]]:
    urls: dict[str, list[str]] = {}

    for relative in DOCS:
        path = ROOT / relative
        if not path.exists():
            continue
        for url, location in iter_markdown_links(path):
            if url.startswith("http://"):
                urls.setdefault(url, []).append(f"{location} uses http")
            elif url.startswith("https://"):
                urls.setdefault(url, []).append(location)
            elif not url.startswith(("http://", "https://")):
                urls.setdefault(url, []).append(location)

    if include_resources:
        resource_path = ROOT / "resources.yml"
        if resource_path.exists():
            for url, location in iter_resource_urls(resource_path):
                urls.setdefault(url, []).append(location)

    return urls


def validate_resource_file() -> list[str]:
    path = ROOT / "resources.yml"
    if not path.exists():
        return ["resources.yml is missing"]

    text = path.read_text(encoding="utf-8")
    required = ["name:", "url:", "type:", "topics:", "cost:", "audience:", "last_checked:", "notes:"]
    errors: list[str] = []
    blocks = re.split(r"\n\s*-\s+name:\s+", text)
    entries = blocks[1:]
    if not entries:
        errors.append("resources.yml has no resource entries")
        return errors

    for index, block in enumerate(entries, start=1):
        normalized = "name: " + block
        for field in required:
            if re.search(rf"^\s*{re.escape(field)}", normalized, re.MULTILINE) is None:
                errors.append(f"resources.yml entry {index} is missing {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true", help="check external URLs over the network")
    parser.add_argument("--include-resources", action="store_true", help="also check URLs in resources.yml")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--sleep", type=float, default=0.05)
    args = parser.parse_args()

    errors = validate_resource_file()
    urls = collect_urls(include_resources=args.include_resources)

    for url, locations in urls.items():
        if url.startswith("http://"):
            errors.append(f"{url} uses http: {', '.join(locations)}")
        elif not (url.startswith("https://") or not url.startswith(("http://", "https://"))):
            errors.append(f"{url} is not an HTTPS or local repository link: {', '.join(locations)}")

    if args.online:
        for url in sorted(u for u in urls if u.startswith("https://")):
            if url in BROWSER_ONLY_URLS:
                print(f"SKIP browser-only {url}")
                continue
            ok, detail = check_url(url, timeout=args.timeout)
            print(f"{'OK' if ok else 'BAD'} {detail} {url}")
            if not ok:
                errors.append(f"{url} failed link check ({detail}): {', '.join(urls[url])}")
            time.sleep(args.sleep)

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Checked {len(urls)} unique URLs/links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
