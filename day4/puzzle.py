from pathlib import Path

input_file = Path(__file__).resolve().parent / "input.txt"

x_positions: list[tuple] = set()
m_positions: list[tuple] = set()
puzzle: dict[tuple, str] = {}


with open(input_file) as f:
    row = 0
    while line := f.readline().strip():
        for col, char in enumerate(line):
            if char == "X":
                x_positions.add((row, col))
            if char == "M":
                m_positions.add((row, col))
            puzzle[(row, col)] = char
        row += 1


def get_number_xmas(puzzle: dict[tuple, str], position: tuple) -> int:
    number_xmas = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for x_change, y_change in directions:
        current_position = position
        valid = True
        for next_letter in "MAS":
            current_position = (
                current_position[0] + x_change,
                current_position[1] + y_change,
            )
            if puzzle.get(current_position) != next_letter:
                valid = False
                break
        number_xmas += valid
    return number_xmas


number_xmas = 0
while x_positions:
    next_position = x_positions.pop()
    number_xmas += get_number_xmas(puzzle, next_position)

print(number_xmas)


def get_number_cross_mas(puzzle: dict[tuple, str], position: tuple) -> int:
    number_cross_mas = 0
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    for x_change, y_change in directions:
        current_position = position
        valid = True
        for next_letter in "AS":
            current_position = (
                current_position[0] + x_change,
                current_position[1] + y_change,
            )
            if puzzle.get(current_position) != next_letter:
                valid = False
                break

        if not valid:
            continue

        initial_x, initial_y = position
        if (
            puzzle.get((initial_x + x_change * 2, initial_y)) == "M"
            and puzzle.get((initial_x, initial_y + y_change * 2)) == "S"
        ):
            number_cross_mas += 1
        if (
            puzzle.get((initial_x, initial_y + y_change * 2)) == "M"
            and puzzle.get((initial_x + x_change * 2, initial_y)) == "S"
        ):
            number_cross_mas += 1

    return number_cross_mas


number_cross_mas = 0
while m_positions:
    next_position = m_positions.pop()
    number_cross_mas += get_number_cross_mas(puzzle, next_position)
print(number_cross_mas // 2)
