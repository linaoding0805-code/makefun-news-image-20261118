#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

Writes the front-page image to the output directory. The program just
copies the image file that ships in this repository, so every run writes
the exact same bytes. The image (entry.png, 1024x1024, under 1 MiB) sums
up Wednesday 18 November 2026 in four stories: the Kerch Bridge road span
collapsing after Ukrainian strikes, Iran's drone strikes on US bases in
Kuwait and Bahrain after the US hit a missile site on Qeshm Island, Xi
and Putin meeting in Shenzhen ahead of Thursday's three-way summit with
Trump, and Mary Peltola winning Alaska to give Democrats a 56-44 Senate
majority. A ticker adds the measles, Ebola and Nvidia stories.
"""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))


def main():
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(BASE, "entry.png"),
        os.path.join(dest_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
