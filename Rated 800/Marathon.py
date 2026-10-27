test_cases = int(input())
flag = 0
for _ in range(test_cases):
    seq = list(map(int, input().split()))
    for i in range(1, 4):
        if seq[i] > seq[0]:
            flag += 1
    print(flag)
    flag = 0
