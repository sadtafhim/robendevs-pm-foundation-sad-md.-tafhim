#!/usr/bin/env python3
"""
Generate a complete, clickable folder/file navigation section in README.md
from a GitHub repository's file tree.

Usage:
    1. Put this script in the root of your cloned repository.
    2. Add the start/end markers to README.md (see below).
    3. Run: python generate_readme.py

README markers (place where you want the navigation to appear):

<!-- AUTO-GENERATED-CONTENTS-START -->

<!-- AUTO-GENERATED-CONTENTS-END -->

The script updates only the content between those markers.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

OWNER = "sadtafhim"
REPO = "robendevs-pm-foundation-sad-md.-tafhim"
README_FILE = Path("README.md")

START_MARKER = "<!-- AUTO-GENERATED-CONTENTS-START -->"
END_MARKER = "<!-- AUTO-GENERATED-CONTENTS-END -->"

# Optional: set GITHUB_TOKEN as an environment variable to increase API limits.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")


def github_get_json(url: str) -> dict[str, Any]:
    """Fetch JSON from GitHub's REST API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "README-Navigation-Generator",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"GitHub API returned HTTP {exc.code}: {details}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not connect to GitHub: {exc}") from exc


def encode_path(path: str) -> str:
    """URL-encode a repository path while preserving folder separators."""
    return urllib.parse.quote(path, safe="/")


def get_repository_tree() -> tuple[str, list[dict[str, Any]]]:
    """Get the default branch and its complete recursive Git tree."""
    api_root = f"https://api.github.com/repos/{OWNER}/{REPO}"
    repo_info = github_get_json(api_root)

    branch = repo_info["default_branch"]
    encoded_branch = urllib.parse.quote(branch, safe="")
    tree_url = f"{api_root}/git/trees/{encoded_branch}?recursive=1"
    tree_data = github_get_json(tree_url)

    if tree_data.get("truncated"):
        raise RuntimeError(
            "GitHub marked the repository tree as truncated. "
            "The script stopped to avoid generating an incomplete README."
        )

    return branch, tree_data.get("tree", [])


def make_navigation(branch: str, entries: list[dict[str, Any]]) -> str:
    """Build an indented Markdown list of folders and files."""
    lines = [
        "## Complete Repository Navigation",
        "",
        "Browse the repository's folders and files below.",
        "",
    ]

    # Sort folders before files at the same level, then alphabetically.
    sorted_entries = sorted(
        entries,
        key=lambda item: (
            item["path"].count("/"),
            item["path"].lower(),
            0 if item.get("type") == "tree" else 1,
        ),
    )

    for item in sorted_entries:
        path = item.get("path", "")
        item_type = item.get("type")

        if not path or item_type not in {"tree", "blob"}:
            continue

        depth = path.count("/")
        name = path.rsplit("/", 1)[-1]

        if item_type == "tree":
            url = (
                f"https://github.com/{OWNER}/{REPO}/tree/"
                f"{urllib.parse.quote(branch, safe='')}/{encode_path(path)}"
            )
            label = f"**{name}/ **"
        else:
            url = (
                f"https://github.com/{OWNER}/{REPO}/blob/"
                f"{urllib.parse.quote(branch, safe='')}/{encode_path(path)}"
            )
            label = name

        lines.append(f'{"  " * depth}- [{label}]({url})')

    return "\n".join(lines)


def update_readme(generated_content: str) -> None:
    """Replace only the section between the README markers."""
    if not README_FILE.exists():
        raise FileNotFoundError(
            f"{README_FILE} was not found. Run this script from the "
            "repository's root folder."
        )

    readme = README_FILE.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        raise ValueError(
            "README markers were not found. Add these exact lines where "
            "the generated navigation should appear:\n\n"
            f"{START_MARKER}\n\n{END_MARKER}"
        )

    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError(
            "Each README marker must appear exactly once."
        )

    before, remainder = readme.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)

    updated = (
        before
        + START_MARKER
        + "\n\n"
        + generated_content
        + "\n\n"
        + END_MARKER
        + after
    )

    README_FILE.write_text(updated, encoding="utf-8")


def main() -> int:
    print(f"Reading GitHub repository: {OWNER}/{REPO}")

    try:
        branch, entries = get_repository_tree()
        generated_content = make_navigation(branch, entries)
        update_readme(generated_content)
    except (RuntimeError, FileNotFoundError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    file_count = sum(1 for item in entries if item.get("type") == "blob")
    folder_count = sum(1 for item in entries if item.get("type") == "tree")

    print("README navigation updated successfully.")
    print(f"Default branch: {branch}")
    print(f"Folders found: {folder_count}")
    print(f"Files found: {file_count}")
    print("Review README.md, then commit and push your changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
