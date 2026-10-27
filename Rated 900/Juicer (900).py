n, b, d = list(map(int, input().split()))
seq = list(map(int, input().split()))
flag = 0
total = 0
for i in range(n):
    if seq[i] <= b:
        total += seq[i]
    if total > d:
        flag += 1
        total = 0
print(flag)
