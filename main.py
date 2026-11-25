"""Copy the 25 November news image to the grader output directory."""
from os import environ
from pathlib import Path
from shutil import copyfile
from sys import stderr

IMAGE = Path(__file__).parent / "entry.png"


def report(size):
    print(size, file=stderr)


def run():
    if not IMAGE.is_file():
        print("entry.png missing", file=stderr)
        return 1
    folder = Path(environ.get("MAKEFUN_OUTPUT_DIR") or environ.get("OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    saved = folder / IMAGE.name
    copyfile(IMAGE, saved)
    report(saved.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
