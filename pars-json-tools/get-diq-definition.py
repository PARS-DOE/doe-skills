#!/usr/bin/env python3
"""Fetch a PARS DIQ check definition from wiki.pars.doe.gov as clean markdown.

PARS DIQs (Data Integrity and Quality checks) are quality rules applied to
PARS CPP JSON uploads after JSON schema validation. Each DIQ has a 7-digit ID
and belongs to a dataset (DS00-DS21). Documentation lives at
https://wiki.pars.doe.gov/en/DIQs/DS{NN}/{id}.

Usage:
    python3 get-diq-definition.py 9070365         # number-only; dataset inferred
    python3 get-diq-definition.py DS07/9070365    # explicit dataset/number
    python3 get-diq-definition.py --url ...       # any wiki page URL

Exit codes:
    0  Page fetched and rendered
    1  Page not found or HTTP error
    2  Invalid input format
"""

from __future__ import annotations

import argparse
import html
import html.parser
import re
import sys
import urllib.error
import urllib.request
from typing import Optional

WIKI_BASE = "https://wiki.pars.doe.gov"
USER_AGENT = "doe-skills/get-diq-definition (https://github.com/cahaseler/doe-skills)"
TIMEOUT_SECONDS = 30


def resolve_diq_path(diq_id: str) -> tuple[Optional[str], Optional[str]]:
    """Map a DIQ identifier to a wiki path.

    Returns (path, error). Path is in the form 'DIQs/DS07/9070365'.
    """
    trimmed = diq_id.strip()
    if not trimmed:
        return None, "DIQ ID cannot be empty"

    # Explicit form: DS{NN}/{digits}, where NN is 00-21.
    explicit = re.fullmatch(r"DS(0\d|1\d|2[01])/(\d+)", trimmed)
    if explicit:
        return f"DIQs/DS{explicit.group(1)}/{explicit.group(2)}", None

    # Number-only: infer dataset from digits 2-3 (e.g. 9070365 -> DS07).
    # First digit is 1 (single-dataset DIQ) or 9 (cross-dataset DIQ).
    if not re.fullmatch(r"\d+", trimmed):
        return None, (
            "DIQ ID must be a number (e.g. 9070365) or DS{NN}/{number} "
            "(e.g. DS07/9070365)"
        )
    if len(trimmed) < 3:
        return None, "DIQ number must be at least 3 digits to determine dataset"

    dataset_digits = trimmed[1:3]
    if not re.fullmatch(r"0\d|1\d|2[01]", dataset_digits):
        return None, (
            f'Cannot infer dataset from digits 2-3 ("{dataset_digits}"). '
            "Expected 00-21 (DS00-DS21)."
        )

    return f"DIQs/DS{dataset_digits}/{trimmed}", None


def fetch_page(url: str) -> str:
    """Fetch a wiki page and return its HTML body."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset)


class _ContentExtractor(html.parser.HTMLParser):
    """Pull the <template slot="contents">...</template> block out of a page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self._depth = 0
        self._buffer: list[str] = []

    @property
    def html(self) -> str:
        return "".join(self._buffer)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        attr_map = {k: v for k, v in attrs}
        if tag == "template" and attr_map.get("slot") == "contents" and self._depth == 0:
            self._depth = 1
            return
        if self._depth >= 1:
            if tag == "template":
                self._depth += 1
            self._buffer.append(self._format_tag(tag, attrs, self_closing=False))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if self._depth >= 1:
            self._buffer.append(self._format_tag(tag, attrs, self_closing=True))

    def handle_endtag(self, tag: str) -> None:
        if self._depth >= 1:
            if tag == "template":
                self._depth -= 1
                if self._depth == 0:
                    return
            self._buffer.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self._depth >= 1:
            self._buffer.append(data)

    def handle_entityref(self, name: str) -> None:
        if self._depth >= 1:
            self._buffer.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self._depth >= 1:
            self._buffer.append(f"&#{name};")

    @staticmethod
    def _format_tag(
        tag: str,
        attrs: list[tuple[str, Optional[str]]],
        *,
        self_closing: bool,
    ) -> str:
        parts = [tag]
        for key, value in attrs:
            if value is None:
                parts.append(key)
            else:
                parts.append(f'{key}="{html.escape(value, quote=True)}"')
        joined = " ".join(parts)
        return f"<{joined} />" if self_closing else f"<{joined}>"


def extract_contents_html(page_html: str) -> Optional[str]:
    """Return the inner HTML of the content slot, or None if missing."""
    parser = _ContentExtractor()
    parser.feed(page_html)
    body = parser.html.strip()
    return body or None


def extract_page_title(page_html: str) -> Optional[str]:
    """Return the wiki page title from the <title> tag, stripped of suffix."""
    match = re.search(r"<title>([^<]+)</title>", page_html, re.IGNORECASE)
    if not match:
        return None
    title = html.unescape(match.group(1)).strip()
    # Strip "| PARS Wiki" suffix the wiki appends to every page title.
    return re.sub(r"\s*\|\s*PARS Wiki\s*$", "", title)


def html_to_markdown(content_html: str) -> str:
    """Convert the wiki's rendered HTML to a workable markdown approximation.

    Wiki.js produces a consistent, well-structured HTML subset, so a focused
    converter handles it without a heavyweight dependency. Anything we don't
    recognize falls through as plain text.
    """
    md = MarkdownConverter().convert(content_html)
    return _tidy_markdown(md)


class MarkdownConverter(html.parser.HTMLParser):
    """Stream-style HTML -> Markdown converter for Wiki.js output."""

    HEADING_TAGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}
    INLINE_TAGS = {"span", "small", "sup", "sub", "i", "u"}
    SKIP_TAGS = {"script", "style"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._out: list[str] = []
        self._skip_depth = 0
        self._link_stack: list[Optional[str]] = []
        self._list_stack: list[dict[str, int | str]] = []
        self._in_pre = 0
        self._in_code = 0
        self._table: Optional[list[list[str]]] = None
        self._table_row: Optional[list[str]] = None
        self._table_cell: Optional[list[str]] = None
        self._table_in_header = False
        self._table_header_seen = False
        self._blockquote_type: list[str] = []
        self._suppress_anchor = 0

    @property
    def markdown(self) -> str:
        return "".join(self._out)

    def convert(self, text: str) -> str:
        self.feed(text)
        self.close()
        return self.markdown

    # ---- HTMLParser hooks ----

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        attr_map = {k: (v or "") for k, v in attrs}

        if tag in self.SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return

        # The wiki injects an anchor link with class "toc-anchor" inside each
        # heading. It's purely a UI affordance — drop it entirely.
        if tag == "a" and "toc-anchor" in attr_map.get("class", ""):
            self._suppress_anchor += 1
            return
        # SVG-image emoji replacements: <img class="emoji" alt="🤖">. Use the alt.
        if tag == "img" and "emoji" in attr_map.get("class", ""):
            self._emit(attr_map.get("alt", ""))
            return

        if tag in self.HEADING_TAGS:
            self._ensure_blank_line()
            self._emit("#" * self.HEADING_TAGS[tag] + " ")
            return
        if tag == "p":
            self._ensure_blank_line()
            return
        if tag == "br":
            self._emit("  \n")
            return
        if tag == "hr":
            self._ensure_blank_line()
            self._emit("---\n\n")
            return
        if tag in {"strong", "b"}:
            self._emit("**")
            return
        if tag in {"em"}:
            self._emit("*")
            return
        if tag == "code":
            self._in_code += 1
            if not self._in_pre:
                self._emit("`")
            return
        if tag == "pre":
            self._ensure_blank_line()
            self._in_pre += 1
            self._emit("```\n")
            return
        if tag == "a":
            self._link_stack.append(attr_map.get("href"))
            self._emit("[")
            return
        if tag == "ul":
            self._list_stack.append({"type": "ul", "index": 0})
            self._ensure_blank_line()
            return
        if tag == "ol":
            self._list_stack.append({"type": "ol", "index": 0})
            self._ensure_blank_line()
            return
        if tag == "li":
            if not self._list_stack:
                # Defensive: list item without parent list (malformed input).
                self._list_stack.append({"type": "ul", "index": 0})
            frame = self._list_stack[-1]
            indent = "  " * (len(self._list_stack) - 1)
            if frame["type"] == "ol":
                frame["index"] = int(frame["index"]) + 1
                marker = f"{frame['index']}. "
            else:
                marker = "- "
            self._ensure_line_start()
            self._emit(f"{indent}{marker}")
            return
        if tag == "blockquote":
            cls = attr_map.get("class", "")
            kind = "note"
            for known in ("is-success", "is-warning", "is-danger", "is-info"):
                if known in cls:
                    kind = known
                    break
            self._blockquote_type.append(kind)
            self._ensure_blank_line()
            return
        if tag == "table":
            self._table = []
            self._table_header_seen = False
            self._ensure_blank_line()
            return
        if tag == "thead":
            self._table_in_header = True
            return
        if tag == "tr" and self._table is not None:
            self._table_row = []
            return
        if tag in {"th", "td"} and self._table_row is not None:
            self._table_cell = []
            return
        # Inline / passthrough tags: leave content unchanged.
        if tag in self.INLINE_TAGS or tag in {"div", "section", "article", "main"}:
            return
        # Unknown tag: ignore the tag itself; content still flows through.

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS:
            if self._skip_depth:
                self._skip_depth -= 1
            return
        if self._skip_depth:
            return

        if tag == "a":
            if self._suppress_anchor:
                self._suppress_anchor -= 1
                return
            href = self._link_stack.pop() if self._link_stack else None
            href = self._normalize_href(href) if href else ""
            self._emit(f"]({href})")
            return
        if tag in self.HEADING_TAGS:
            self._emit("\n\n")
            return
        if tag == "p":
            self._emit("\n\n")
            return
        if tag in {"strong", "b"}:
            self._emit("**")
            return
        if tag == "em":
            self._emit("*")
            return
        if tag == "code":
            if self._in_code:
                self._in_code -= 1
            if not self._in_pre:
                self._emit("`")
            return
        if tag == "pre":
            if self._in_pre:
                self._in_pre -= 1
            self._emit("\n```\n\n")
            return
        if tag == "li":
            self._emit("\n")
            return
        if tag in {"ul", "ol"}:
            if self._list_stack:
                self._list_stack.pop()
            if not self._list_stack:
                self._emit("\n")
            return
        if tag == "blockquote":
            if self._blockquote_type:
                self._blockquote_type.pop()
            self._emit("\n")
            return
        if tag == "table":
            self._flush_table()
            return
        if tag == "thead":
            self._table_in_header = False
            return
        if tag == "tr" and self._table is not None:
            if self._table_row is not None:
                self._table.append(self._table_row)
                if self._table_in_header:
                    self._table_header_seen = True
                self._table_row = None
            return
        if tag in {"th", "td"} and self._table_row is not None and self._table_cell is not None:
            self._table_row.append("".join(self._table_cell).strip())
            self._table_cell = None
            return

    def handle_data(self, data: str) -> None:
        if self._skip_depth or self._suppress_anchor:
            return
        if self._table_cell is not None:
            # Collapse newlines inside a table cell — markdown tables are one-row-per-line.
            self._table_cell.append(re.sub(r"\s+", " ", data))
            return
        if self._in_pre:
            self._out.append(data)
            return
        if self._blockquote_type:
            text = data
            # Inject "> " at the start of each new line inside a blockquote.
            if self._out and self._out[-1].endswith("\n"):
                text = "> " + text
            text = text.replace("\n", "\n> ")
            self._out.append(text)
            return
        self._out.append(data)

    # ---- helpers ----

    def _emit(self, text: str) -> None:
        if self._table_cell is not None:
            self._table_cell.append(text)
            return
        if self._blockquote_type and not self._in_pre:
            if self._out and self._out[-1].endswith("\n"):
                text = "> " + text
            text = text.replace("\n", "\n> ")
        self._out.append(text)

    def _ensure_blank_line(self) -> None:
        if not self._out:
            return
        tail = "".join(self._out[-3:])
        if tail.endswith("\n\n"):
            return
        if tail.endswith("\n"):
            self._out.append("\n")
        else:
            self._out.append("\n\n")

    def _ensure_line_start(self) -> None:
        if not self._out:
            return
        tail = "".join(self._out[-2:])
        if not tail.endswith("\n"):
            self._out.append("\n")

    def _normalize_href(self, href: str) -> str:
        if href.startswith("/"):
            return WIKI_BASE + href
        return href

    def _flush_table(self) -> None:
        rows = self._table or []
        self._table = None
        if not rows:
            return
        # If no explicit header was seen, treat the first row as the header.
        if not self._table_header_seen:
            header, *body = rows
        else:
            header, *body = rows[0], *rows[1:]
        width = max(len(header), max((len(r) for r in body), default=0))
        header = header + [""] * (width - len(header))
        body = [row + [""] * (width - len(row)) for row in body]
        self._out.append("| " + " | ".join(header) + " |\n")
        self._out.append("|" + "|".join([" --- "] * width) + "|\n")
        for row in body:
            self._out.append("| " + " | ".join(row) + " |\n")
        self._out.append("\n")


def _tidy_markdown(text: str) -> str:
    # Strip the "AI-generated, unreviewed" banner the wiki injects into many
    # DIQs. The banner is a blockquote starting with a robot emoji and the
    # phrase "The following text was generated by an AI tool". The whole
    # blockquote (all consecutive "> " lines, plus any trailing blank quoted
    # lines) is removed.
    text = re.sub(
        r"(?:^|\n)(?:> [^\n]*The following text was generated by an AI tool[^\n]*\n)"
        r"(?:>[^\n]*\n)*"
        r"(?:>\s*\n)*",
        "\n",
        text,
    )
    # Drop any stray empty blockquote frames (`> \n> \n`) left over from
    # other removals.
    text = re.sub(r"(?:^|\n)(?:>\s*\n){2,}", "\n", text)
    # Pull list item text up onto the same line as its marker:
    # "1. \n\nFoo" -> "1. Foo", "- \n\nFoo" -> "- Foo".
    text = re.sub(r"^(\s*(?:[-*]|\d+\.)) +\n\n+", r"\1 ", text, flags=re.MULTILINE)
    # Headings shouldn't carry a leading space inside the "# " prefix from a
    # dropped anchor link: "##  Heading" -> "## Heading".
    text = re.sub(r"^(#{1,6})  +", r"\1 ", text, flags=re.MULTILINE)
    # Collapse 3+ blank lines down to 2.
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def render_page(page_html: str, source_url: str) -> str:
    title = extract_page_title(page_html) or "Untitled"
    contents_html = extract_contents_html(page_html)
    if not contents_html:
        raise ValueError("Could not find page contents in wiki response")

    body = html_to_markdown(contents_html)
    return f"# {title}\n\nSource: {source_url}\n\n{body}"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "diq_id",
        nargs="?",
        help='DIQ id (e.g. "9070365" or "DS07/9070365"). Omit when using --url.',
    )
    parser.add_argument(
        "--url",
        help="Fetch an arbitrary wiki.pars.doe.gov page URL instead of resolving a DIQ id.",
    )
    args = parser.parse_args(argv)

    if args.url:
        url = args.url
    else:
        if not args.diq_id:
            parser.error("provide a DIQ id or --url URL")
        path, error = resolve_diq_path(args.diq_id)
        if error:
            print(f"Error: {error}", file=sys.stderr)
            return 2
        url = f"{WIKI_BASE}/en/{path}"

    try:
        page_html = fetch_page(url)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            print(f"Error: DIQ not found at {url}", file=sys.stderr)
            return 1
        print(f"Error: HTTP {exc.code} fetching {url}: {exc.reason}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"Error: could not reach wiki.pars.doe.gov: {exc.reason}", file=sys.stderr)
        return 1

    try:
        rendered = render_page(page_html, url)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
