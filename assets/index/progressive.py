#!/usr/bin/env python3

import subprocess
from pathlib import Path

targets = {
    "20241111_104352.jpg",
    "20260219_203530.jpg",
    "20241226_152038.jpg",
    "20251224_203218.jpg",
    "20250616_150945.jpg",
    "20251121_182006.jpg",
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
