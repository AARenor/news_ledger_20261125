from os import environ
from pathlib import Path
from shutil import copyfile
from sys import stderr

PICTURE = Path(__file__).parent / "entry.png"


def run() -> int:
    if not PICTURE.is_file():
        print("entry.png missing", file=stderr)
        return 1

    folder = Path(
        environ.get("MAKEFUN_OUTPUT_DIR")
        or environ.get("OUTPUT_DIR")
        or "/output"
    )
    folder.mkdir(parents=True, exist_ok=True)
    saved = folder / PICTURE.name
    copyfile(PICTURE, saved)
    print(saved.stat().st_size, file=stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
