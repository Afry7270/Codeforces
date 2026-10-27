test_cases = int(input())
seq = [None]
max_seq = 0
for i in range(test_cases):
    sup = int(input())
    seq.append(sup)
for i in range(1, test_cases+1):
    flag = 0
    while seq[i] != -1:
        flag += 1
        i = seq[i]
    max_seq = max(max_seq, flag)
print(max_seq + 1)
