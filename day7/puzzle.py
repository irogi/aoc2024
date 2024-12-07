from pathlib import Path
from itertools import product

input_file = Path(__file__).resolve().parent / "input.txt"


def evaluate_expression(vals: list[int], ops: list[str]) -> int:
    result = vals[0]
    for i, op in enumerate(ops):
        if op == "+":
            result = result + vals[i + 1]
        if op == "*":
            result = result * vals[i + 1]
        if op == "||":
            result = int(str(result) + str(vals[i + 1]))
    return result


def can_permutate(total: int, vals: list[int], valid_ops=["+", "*"]) -> bool:
    for ops in product(valid_ops, repeat=len(vals) - 1):
        if evaluate_expression(vals, list(ops)) == total:
            return True
    return False


rows = []
with open(input_file) as f:
    while line := f.readline().strip():
        total, vals = line.split(": ")
        rows.append((int(total), list(map(int, vals.split()))))

p1_score = 0
p2_score = 0
for total, vals in rows:
    if can_permutate(total, vals):
        p1_score += total

    if can_permutate(total, vals, ["+", "*", "||"]):
        p2_score += total

print(p1_score)
print(p2_score)
