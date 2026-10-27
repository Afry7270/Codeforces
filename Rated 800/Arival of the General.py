soldier_no = int(input())
soldier_seq = list(map(int, input().split()))
min_height = soldier_seq[soldier_no-1]
max_height = soldier_seq[0]

for height in soldier_seq:
    if height < min_height:
        min_height = height
for height in soldier_seq:
    if height > max_height:
        max_height = height
min_index = None
max_index = soldier_seq.index(max_height)

for i in range(soldier_no):
    if soldier_seq[i] == min_height:
        min_index = i
if min_index < max_index:
    print(max_index + (soldier_no-min_index) - 2)
else:
    print(max_index + (soldier_no-min_index) - 1)


