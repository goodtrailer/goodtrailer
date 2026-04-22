#!/usr/bin/env python3

import subprocess
from pathlib import Path

targets = {
    "20260409_205258.jpg",
    "20260409_205330.jpg",
    "20260327_202215.jpg",
}

if len(targets) == 0:
    print("No targets! Edit source file.")

Path("prog").mkdir(exist_ok=True)
for file in targets:
    cmd = ["jpegtran", "-progressive", file, f"prog/{file}"]
    print(f"Processing: {file}")

    try:
        subprocess.run(cmd, check=True)
        print(f"    Done: {file}")
    except subprocess.CalledProcessError as e:
        print(f"    Failed: {file} (Error: {e})")
    except FileNotFoundError:
        print("    Error: \"jpegtran\" not found")
        break
