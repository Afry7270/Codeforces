seq = list(map(int, input().split()))
puzzles = list(map(int, input().split()))
puzzles.sort()
minimum = abs(puzzles[0] - puzzles[seq[0] - 1])
for i in range(0, len(puzzles) - seq[0] + 1):
    value = abs(puzzles[i] - puzzles[i + seq[0] - 1])
    if value < minimum:
        minimum = value
print(minimum)