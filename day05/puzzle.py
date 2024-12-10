from collections import defaultdict
from pathlib import Path

input_file = Path(__file__).resolve().parent / "input.txt"

rows = []
rules: dict[int, set[int]] = defaultdict(set)


def get_sort_key(rules: dict[int, set[int]], keys: set[int]) -> dict[int, int]:
    sorted_keys = []
    remaining_rules = {k: rules[k] & keys for k in keys}

    while remaining_rules:
        smallest = set(remaining_rules) - set().union(*remaining_rules.values())
        sorted_keys.extend(smallest)
        for v in smallest:
            remaining_rules.pop(v)

    # largest never appears in the rules
    largest = set().union(*rules.values()) - set(sorted_keys)
    sorted_keys.extend(largest)

    return {key: i for i, key in enumerate(sorted_keys)}


sorted_score, unsorted_score = 0, 0
with open(input_file) as f:
    while line := f.readline().strip():
        before, after = (int(i) for i in line.split("|"))
        rules[before].add(after)

    while line := f.readline().strip():
        row = [int(i) for i in line.split(",")]

        # sort_key is circular on full ruleset
        sort_key = get_sort_key(rules, keys=set(row))

        sorted_row = sorted(row, key=lambda v: sort_key[v])
        score = sorted_row[len(row) // 2]
        if row == sorted_row:
            sorted_score += score
        else:
            unsorted_score += score

print(sorted_score)
print(unsorted_score)
