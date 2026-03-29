from __future__ import annotations

import shutil
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def workspace_root() -> Path:
    return repo_root().parent


def copy_tree(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def main() -> int:
    root = repo_root()
    workspace = workspace_root()
    copy_tree(workspace / "ShellRPG-www" / "public" / "media", root / "assets" / "www" / "public" / "media")
    copy_tree(workspace / "ShellRPG-www" / "assets" / "manifest", root / "manifests" / "www")
    copy_tree(workspace / "ShellRPG-client" / "media", root / "assets" / "client" / "media")
    print("ShellRPG-cdn assets synchronized from workspace endpoints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
