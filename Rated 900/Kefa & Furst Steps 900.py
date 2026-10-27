days = int(input())
seq = list(map(int, input().split()))
total = 1
num = 1
for i in range(0, days-1):
    if seq[i] <= seq[i+1]:
        total += 1
        if total > num:
            num = total
    else:
        total = 1
print(num)

