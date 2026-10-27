test_cases = int(input())
for i in range(test_cases):
    h, n, m = list(map(int, input().split()))
    while True:
        if h > 20 and n != 0:
            h = (h // 2) + 10
            n -= 1
        else:
            break
    print(["YES", "NO"][h > m*10])








