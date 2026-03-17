#!/usr/bin/env python3

import subprocess
from pathlib import Path

targets = {
    "20260219_203530.jpg",
    "20250616_150945.jpg",
    "20251224_203218.jpg",
    "20250616_150945.jpg",
    "20241226_152038.jpg",
    "20241111_104352.jpg",
}

if len(targets) == 0:
    print("No targets! Edit source file.")

Path("rot").mkdir(exist_ok=True)
for file in targets:
    cmd = ["jpegtran", "-progressive", "-rotate", "90", str(file), f"rot/{file}"]
    print(f"Processing: {file}")

    try:
        subprocess.run(cmd, check=True)
        print(f"    Done: {file}")
    except subprocess.CalledProcessError as e:
        print(f"    Failed: {file} (Error: {e})")
    except FileNotFoundError:
        print("    Error: \"jpegtran\" not found")
        break
