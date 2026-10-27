room_no = int(input())
room_matrix = [list(map(int, input().split())) for _ in range(room_no)]
count = 0
for i in room_matrix:
    if i[1] - i[0] >= 2:
        count += 1
print(count)
