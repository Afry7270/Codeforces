test_cases = int(input())
for i in range(test_cases):
    n, k = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    seq.sort()
    flag = 0
    maximum = 0
    for j in range(n - 1):
        if (seq[j + 1] - seq[j]) <= k:
            flag += 1
            if flag > maximum:
                maximum = flag
        else:
            flag = 0
    print(n-(maximum+1))
