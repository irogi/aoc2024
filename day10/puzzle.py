from pathlib import Path

input_file = Path(__file__).resolve().parent / "input.txt"


def num_9s(map: dict[tuple, int], start_position: tuple[int, int]) -> int:
    valid_9s = set()
    stack = [start_position]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        current_position = stack.pop()
        for x_change, y_change in directions:
            new_position = (
                current_position[0] + x_change,
                current_position[1] + y_change,
            )
            if new_position not in map:
                continue
            height = map[current_position]

            if height == 9:
                valid_9s.add(current_position)

            if height + 1 == map[new_position]:
                stack.append(new_position)

    return len(valid_9s)


def num_paths(map: dict[tuple, int], start_position: tuple[int, int]) -> int:
    valid_paths = set()
    stack = [
        (start_position,),
    ]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        current_path = stack.pop()
        current_position = current_path[-1]
        for x_change, y_change in directions:
            new_position = (
                current_position[0] + x_change,
                current_position[1] + y_change,
            )
            if new_position not in map:
                continue
            height = map[current_position]

            if height == 9:
                valid_paths.add((*current_path, current_position))

            if height + 1 == map[new_position]:
                stack.append((*current_path, new_position))

    return len(valid_paths)


map: dict[tuple, int] = {}
start_positions = []
with open(input_file) as f:
    row = 0
    while line := f.readline().strip():
        for col, char in enumerate(line):
            map[(row, col)] = int(char)
            if char == "0":
                start_positions.append((row, col))
        row += 1

score_p1 = 0
score_p2 = 0
for start_position in start_positions:
    score_p1 += num_9s(map, start_position)
    score_p2 += num_paths(map, start_position)

print(score_p1)
print(score_p2)
