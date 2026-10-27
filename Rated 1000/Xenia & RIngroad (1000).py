m, n = list(map(int,input().split()))
seq = list(map(int, input().split()))
seq.insert(0, 1)
time = 0
for i in range(n):
    if seq[i + 1] < seq[i]:
        time += m - seq[i] + seq[i + 1]
    else:
        time += seq[i + 1] - seq[i]
print(time)
