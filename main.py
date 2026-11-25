import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).with_name("entry.png")


def main() -> int:
    if not SOURCE.is_file():
        print("entry.png missing", file=sys.stderr)
        return 1
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target_dir / "entry.png")
    print((target_dir / "entry.png").stat().st_size, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
