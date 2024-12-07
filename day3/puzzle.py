import re


def get_score(s: str) -> int:
    return sum(int(i) * int(j) for (i, j) in re.findall(r"mul\((\d+),(\d+)\)", s))


def get_matching_indices(s: str, term: str) -> list[int]:
    return [m.start() for m in re.finditer(term, s)]


program = ""

with open("input.txt") as f:
    while line := f.readline().strip():
        program += line

print(get_score(program))

enabled_mapping = {}
for index in get_matching_indices(program, "do()"):
    enabled_mapping[index] = True
for index in get_matching_indices(program, "don't()"):
    enabled_mapping[index] = False

p2_score = 0
start_index = 0
is_active = True

for index in sorted(enabled_mapping.keys()):
    should_enable = enabled_mapping[index]
    if is_active and not should_enable:
        p2_score += get_score(program[start_index:index])
        is_active = False
    elif not is_active and should_enable:
        start_index = index
        is_active = True
    else:
        # ignore double enable/disable commands
        pass
print(p2_score)
