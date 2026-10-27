input_seq = list(map(int, input().split()))
time = 240 - input_seq[1]
total = 0
count = 0
for i in range(1, input_seq[0]+1):
    total += i*5
    if total > time:
        break
    else:
        count += 1
print(count)

