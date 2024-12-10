def get_changes(lst):
    changes = [lst[i] - lst[i + 1] for i in range(len(lst) - 1)]
    return changes


def is_safe(lst):
    changes = get_changes(lst)
    return all(0 < c <= 3 for c in changes) or all(-3 <= c < 0 for c in changes)


safe_count = 0
relaxed_safe_count = 0

with open("input.txt") as f:
    while line := f.readline().strip():
        vals = [int(v) for v in line.split()]

        increment_safe = is_safe(vals)
        increment_relaxed_safe = False

        for i in range(len(vals)):
            if is_safe(vals[:i] + vals[i + 1 :]):
                increment_relaxed_safe = True

        safe_count += increment_safe
        relaxed_safe_count += increment_relaxed_safe


print(safe_count)
print(relaxed_safe_count)
