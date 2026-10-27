people = int(input())
seq = list(map(int, input().split()))
max_num = max(seq)
total = 0
for i in range(people):
    total = total + (max_num - seq[i])
print(total)
