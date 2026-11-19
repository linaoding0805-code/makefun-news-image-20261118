"""Front-page entry for 18 November 2026.

Drops the shipped front-page picture into the output folder untouched,
so every run emits byte-identical output.
"""
from pathlib import Path

PICTURE = Path(__file__).resolve().with_name("entry.png")


def place_picture(folder):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.png").write_bytes(PICTURE.read_bytes())


def run():
    import os

    # The output directory comes from the harness; /output is the default.
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    place_picture(destination)


run()
