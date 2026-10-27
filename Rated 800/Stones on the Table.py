stone_no = int(input())
stone_sequence = list(input())
count = 0
for i in range(1, stone_no):
    if stone_sequence[i] == stone_sequence[i-1]:
        count += 1
print(count)
