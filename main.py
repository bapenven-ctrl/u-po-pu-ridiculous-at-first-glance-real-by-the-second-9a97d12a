#!/usr/bin/env python3
"""Write one startup pitch sentence to /output/entry.txt.

The pitch: ad space on the bottom of swimming pools.
Deterministic: the same constant text on every run.
No network, no environment, no dependencies outside this repository.
"""
import os

PITCH = "We sell ad space on the bottom of pools - swimmers stare at it lap after lap, and brands pay $500 a month for the only billboard nobody can scroll past."

def main():
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
