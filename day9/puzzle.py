from pathlib import Path

input_file = Path(__file__).resolve().parent / "input.txt"


def decode_line(line):
    decoded_line = []
    for i in range(0, len(line), 2):
        decoded_line += [i // 2] * int(line[i])
        if i + 1 < len(line):
            decoded_line += [None] * int(line[i + 1])
    return decoded_line


def compress_line(line):
    compressed_line = []
    l, r = 0, len(line) - 1
    while l < r + 1:
        if line[l] is not None:
            compressed_line.append(line[l])
            l += 1
        elif line[r] is not None:
            compressed_line.append(line[r])
            r -= 1
            l += 1
        else:
            r -= 1

    return compressed_line


def compress_line_2(disk):
    file_map: dict[int, tuple] = {}
    n = len(disk)
    i = 0
    while i < n:
        if disk[i]:
            f_id = disk[i]
            start = i
            while i < n and disk[i] == f_id:
                i += 1
            length = i - start
            file_map[f_id] = (start, length)
        else:
            i += 1

    file_ids = sorted(file_map.keys(), reverse=True)

    def find_free_segment_to_left(file_start, file_length):
        end_limit = file_start
        idx = 0
        while idx < end_limit:
            if disk[idx] is None:
                run_start = idx
                while idx < end_limit and disk[idx] is None:
                    idx += 1
                run_length = idx - run_start
                if run_length >= file_length:
                    return run_start
            else:
                idx += 1
        return None

    def move_file(f_id):
        original_start, f_length = file_map[f_id]
        new_start = find_free_segment_to_left(original_start, f_length)
        if new_start is None:
            return

        file_blocks = disk[original_start : original_start + f_length]

        for i in range(f_length):
            disk[new_start + i] = file_blocks[i]

        for i in range(f_length):
            disk[original_start + i] = None

        file_map[f_id] = (new_start, f_length)

    for f_id in file_ids:
        move_file(f_id)

    return disk


def get_checksum(line):
    line = [v or 0 for v in line]
    return sum(int(val) * i for i, val in enumerate(line))


with open(input_file) as f:
    while line := f.readline().strip():
        decoded_line = decode_line(line)
        compressed_line = compress_line(decoded_line)
        compressed_line_2 = compress_line_2(decoded_line)


print(get_checksum(compressed_line))
print(get_checksum(compressed_line_2))
