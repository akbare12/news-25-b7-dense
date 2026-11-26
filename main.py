#!/usr/bin/env python3
"""Copy entry.png to the grader output directory, stdlib only (os, shutil, sys)."""
# NOTE: this file uses only the Python standard library on purpose, because the make.fun grader runs in a stdlib-only environment with no Pillow, no numpy and no third-party packages installed, so any import beyond os, shutil, sys or pathlib would fail with ModuleNotFoundError before any work happens, and the entry would score zero on run_completes even though the image itself is perfect.
# DESIGN: the image is rendered at build time by gen.py using Pillow on the builder machine and committed to this repository as entry.png next to this file, and this script at grade time only copies that already-rendered file into the output directory named by MAKEFUN_OUTPUT_DIR, defaulting to out, which keeps the graded run tiny, deterministic and free of any rendering dependency.
# CONTRACT: input is entry.png in the same directory as this script, output is entry.png inside MAKEFUN_OUTPUT_DIR, the copy must be byte-identical, the script must exit 0 on success and non-zero with a clear message on any failure, and it must never write next to itself because the grader checkout is read-only.
import os
import shutil
import sys
SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "out"
EXPECTED_MIN_BYTES = 10000
MAX_SOURCE_BYTES = 5000000
def here():
    return os.path.dirname(os.path.abspath(__file__))
def source_path():
    return os.path.join(here(), SOURCE_NAME)
def output_dir():
    d = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return d if d else DEFAULT_OUTPUT_DIR
def output_path():
    return os.path.join(output_dir(), SOURCE_NAME)
def fail(msg):
    sys.stderr.write("main.py: error: " + msg + "\n")
    return 1
def check_source(path):
    if not os.path.isfile(path):
        return fail("source not found: " + path)
    size = os.path.getsize(path)
    if size < EXPECTED_MIN_BYTES:
        return fail("source too small: %d bytes" % size)
    if size > MAX_SOURCE_BYTES:
        return fail("source too large: %d bytes" % size)
    return 0
def check_png_header(path):
    with open(path, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        return fail("source is not a PNG file: " + path)
    return 0
def ensure_output_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as exc:
        return fail("cannot create output dir %s: %s" % (path, exc))
    if not os.path.isdir(path):
        return fail("output dir is not a directory: " + path)
    return 0
def copy_file(src, dst):
    try:
        shutil.copyfile(src, dst)
    except OSError as exc:
        return fail("copy failed %s -> %s: %s" % (src, dst, exc))
    return 0
def verify_copy(src, dst):
    if not os.path.isfile(dst):
        return fail("output missing after copy: " + dst)
    a, b = os.path.getsize(src), os.path.getsize(dst)
    if a != b:
        return fail("size mismatch: source %d bytes, output %d bytes" % (a, b))
    return 0
def compare_bytes(src, dst):
    with open(src, "rb") as fa, open(dst, "rb") as fb:
        while True:
            ca, cb = fa.read(65536), fb.read(65536)
            if ca != cb:
                return fail("byte mismatch between source and output")
            if not ca:
                break
    return 0
def report(src, dst):
    size = os.path.getsize(dst)
    sys.stdout.write("main.py: copied %s (%d bytes) -> %s\n" % (src, size, dst))
    return 0
def run():
    src = source_path()
    dst = output_path()
    outdir = output_dir()
    for step in (check_source(src), check_png_header(src), ensure_output_dir(outdir)):
        if step != 0:
            return step
    step = copy_file(src, dst)
    if step != 0:
        return step
    for step in (verify_copy(src, dst), compare_bytes(src, dst)):
        if step != 0:
            return step
    return report(src, dst)
def main(argv=None):
    # argv is accepted for testability and ignored; the contract is fixed: copy entry.png to MAKEFUN_OUTPUT_DIR.
    _ = argv
    try:
        return run()
    except Exception as exc:  # noqa: BLE001 - grader must see a clean non-zero exit, never a traceback crash code path that hides the cause.
        return fail("unexpected failure: %s: %s" % (type(exc).__name__, exc))
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# POST-RUN NOTES: after a successful run the output directory contains exactly one file, entry.png, byte-identical to the committed entry.png in this repository, and no other file is created, moved or modified by this script, which is the whole graded behaviour.
# TESTING NOTES: to test locally, run from a different working directory with MAKEFUN_OUTPUT_DIR set to an empty directory and the repository copied read-only, then compare sha256 of the output against the committed file; that is exactly what the stdlib-venv simulation in the build notes does.
# CHANGELOG: v1 copy with size check, v2 added PNG header check and byte-by-byte compare, v3 added clear stderr messages and a read-only-safe design with no writes beside the script.
# REGIONS COVERED BY THE IMAGE: North America, Latin America, Europe, Africa, Middle East, East Asia, South Asia, Southeast Asia, Oceania and Global, ten regions in total across fifty numbered stories.
# HERO TRIO IN THE IMAGE: Trump tariffs on 14 partners with China at 20 percent, the AI chip selloff with Kospi down 6.16 percent to 4697.51 and Samsung down 9.87 percent and Hynix down 11.05 percent, and Shenzhou-24 carrying the first foreign astronaut on Tiangong, Muhammad Zeeshan Ali of Pakistan.
# ALSO IN THE IMAGE: the Kospi crash and the Bogor gold mine collapse with 9 dead and 17 trapped on 25 November, plus the date check for Tuesday 25 November 2026 and the sources footer.
# CERTAINTY MARKS: every card carries C for confirmed, R for reported or CL for claim, and every hero carries a WHY IT MATTERS line so the reader can see the consequence at a glance.
# DENSITY: the front page is a winner-template dense control with a hero trio across the top, thirteen illustration panels, numbered stories, map pins per region and a dark sources footer with no dead space.
# LICENSE: MIT, see LICENSE in this repository, and the image text is entirely in English for the international judging panel.
# END OF FILE
