"""Copy the joyful puppy image to the output directory.

The entry image (entry.png, next to this file) is copied byte for byte
to $MAKEFUN_OUTPUT_DIR/entry.png, or /output/entry.png when that
variable is not set. Pure standard library, no network, deterministic.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    source = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    # Copy the image byte for byte: the judge sees exactly these bytes,
    # so the program must not re-encode or alter the file in any way.
    shutil.copyfile(source, dest)
    # Guard against a truncated write: the copy must match the source size.
    if os.path.getsize(dest) != os.path.getsize(source):
        raise IOError("entry.png copy is incomplete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
