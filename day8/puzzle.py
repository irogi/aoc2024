from collections import defaultdict
from pathlib import Path
from itertools import product

input_file = Path(__file__).resolve().parent / "input.txt"


def get_antinodes(antennae: tuple[int, int], max_repeats=1) -> list[tuple[int, int]]:
    all_antennae_pairs = list(product(antennae, repeat=2))
    antinodes = set()
    for a1, a2 in all_antennae_pairs:
        if a1 == a2:
            continue
        distance_x = a1[0] - a2[0]
        distance_y = a1[1] - a2[1]
        new_antinodes = set()
        for i in range(1, max_repeats + 1):
            new_antinodes |= {
                (a1[0] + distance_x * i, a1[1] + distance_y * i),
                (a2[0] + distance_x * i, a2[1] + distance_y * i),
                (a1[0] - distance_x * i, a1[1] - distance_y * i),
                (a2[0] - distance_x * i, a2[1] - distance_y * i),
            }
        if max_repeats == 1:
            new_antinodes -= {a1, a2}

        antinodes |= new_antinodes
    return antinodes


frequency_map: dict[str, set[tuple]] = defaultdict(set)
valid_coors = set()
max_repeats = -1
with open(input_file) as f:
    row = 0
    while line := f.readline().strip():
        for col, char in enumerate(line):
            if char != ".":
                frequency_map[char] |= {(row, col)}

            valid_coors |= {(row, col)}
            max_repeats = max(max_repeats, row, col)
        row += 1

all_antinodes_1 = set()
all_antinodes_2 = set()
for _, antennae in frequency_map.items():
    all_antinodes_1 |= get_antinodes(antennae)
    all_antinodes_2 |= get_antinodes(antennae, max_repeats=max_repeats)

# filter out antinodes that are not in the valid coordinates
all_antinodes_1 &= valid_coors
all_antinodes_2 &= valid_coors
print(len(all_antinodes_1))
print(len(all_antinodes_2))
