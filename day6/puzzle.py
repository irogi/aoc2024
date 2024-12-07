from collections import defaultdict
from pathlib import Path

input_file = Path(__file__).resolve().parent / "input.txt"

guard_position: tuple[int, int] = (-1, -1)
course_obstacles: dict[tuple[int, int], bool] = {}
with open(input_file) as f:
    row = 0
    while line := f.readline().strip():
        for col, char in enumerate(line):
            if char == "^":
                guard_position = (row, col)

            course_obstacles[(row, col)] = char == "#"
        row += 1


def get_path_length(
    initial_position: tuple[int, int], course_obstacles: dict[tuple[int, int], bool]
) -> int:
    current_position = initial_position
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    visited = defaultdict(set)
    on_map = True
    orientation = 0
    while on_map:
        visited[current_position].add(orientation)
        direction = directions[orientation]
        next_position = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )

        if visited.get(next_position) and orientation in visited[next_position]:
            # infinite loop
            return -1

        if course_obstacles.get(next_position) is None:
            on_map = False
        elif course_obstacles.get(next_position):
            orientation = (orientation + 1) % 4
        else:
            current_position = next_position

    return len(visited)


print(get_path_length(guard_position, course_obstacles))

options = 0
for key in course_obstacles:
    modified_course = course_obstacles.copy()
    if modified_course[key]:
        continue

    modified_course[key] = True
    if get_path_length(guard_position, modified_course) == -1:
        options += 1

print(options)
