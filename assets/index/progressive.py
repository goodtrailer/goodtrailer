#!/usr/bin/env python3

import subprocess
from pathlib import Path

targets = {
    "20260515_135344.jpg",
    "20260615_111346.jpg",
    "20260616_101537.jpg",
    "20260616_102108.jpg",
    "20260624_100506.jpg",
    "20260712_143600.jpg",
    "20260830_084936.jpg",
    "20260905_150011.jpg",
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
