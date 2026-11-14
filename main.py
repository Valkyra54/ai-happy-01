#!/usr/bin/env python3
"""ai-happy-01 v3 entrypoint.

Takes the bundled entry.png that ships next to this file and places an
exact byte-for-byte copy of it into the grader's output directory.
"""

import os
import shutil
import sys


def output_directory():
    """Return the output directory: $MAKEFUN_OUTPUT_DIR if set, else /output."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)

    target = os.path.join(out_dir, "entry.png")
    # copyfile preserves the bytes exactly; no re-encoding happens here.
    shutil.copyfile(source, target)

    written = os.path.getsize(target)
    print("entry.png copied to %s (%d bytes)" % (target, written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
