import sys
from pathlib import Path
from typing import List, Tuple

# -----------------------------------------------------------
# Problem 1: Combination Lock Simulation
# -----------------------------------------------------------


def compute_password(rotations: List[tuple[str, int]], start: int = 50) -> Tuple[int, int]:
    """
    Simulate the dial and count how many times it lands on 0 and how many 
    times it crosses over 0.
    """
    pos = start 
    landings_only = 0
    passes   = 0

    for direction, distance in rotations:
        # Find wraps for each rotation and new position
        if direction == "R":
            # moving right: every full 100‑step cycle is a wrap
            wraps = (pos + distance - 1) // 100
            pos = (pos + distance) % 100
        else:   # direction == "L"
            if pos == 0:
                # Starting from 0: the FIRST step does NOT cross zero.
                wraps = (distance - 1) // 100
            elif distance > pos:
                # We have to go below 0 → at least one wrap.
                wraps = (distance - pos + 99) // 100
            else:
                wraps = 0
            pos = (pos - distance) % 100

        passes += wraps
           
        if pos == 0:
            landings_only += 1

    return landings_only, passes

if __name__ == "__main__":
    INPUT_PATH = Path(sys.argv[1])
    raw_lines = INPUT_PATH.read_text().splitlines()

    rotations: List[tuple[str, int]] = []
    for line in raw_lines:
        dir_char = line[0]
        dist = int(line[1:])
        rotations.append((dir_char, dist))

    hits, passes = compute_password(rotations)

    print("Part 1 passcode based on landing on zero:", hits)
    print("Part 2 passcode based on crossing zero:", passes + hits)
