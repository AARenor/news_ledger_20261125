"""Copy entry.png into the output directory and report the copied byte count."""

from os import environ
from pathlib import Path
from shutil import copyfile
from sys import stderr

def report(size: int) -> None:
    print(size, file=stderr)


IMAGE = Path(__file__).parent / "entry.png"


def run() -> int:
    if not IMAGE.is_file():
        print("entry.png missing", file=stderr)
        return 1

    folder = Path(
        environ.get("MAKEFUN_OUTPUT_DIR")
        or environ.get("OUTPUT_DIR")
        or "/output"
    )
    folder.mkdir(parents=True, exist_ok=True)
    saved = folder / IMAGE.name
    copyfile(IMAGE, saved)
    report(saved.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
