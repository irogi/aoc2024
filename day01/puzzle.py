from collections import Counter


col1, col2 = [], []
with open("input.txt") as f:
    while line := f.readline().strip():
        v1, v2 = line.split()
        col1.append(int(v1))
        col2.append(int(v2))

col1 = sorted(col1)
col2 = sorted(col2)

distances = sum(abs(a - b) for a, b in zip(col1, col2))
print(distances)

col2_counts = Counter(col2)
occurance_sum = sum(c1 * col2_counts[c1] for c1 in col1)

print(occurance_sum)
