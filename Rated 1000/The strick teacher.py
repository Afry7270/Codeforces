for _ in range(int(input())):
    seq = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    a = int(input())
    if b[0] < a < b[1]:
        maxi = max((a - b[0]), (b[1] - a))
        mini = min((a - b[0]), (b[1] - a))
        print(maxi//2 + mini // 2)
    if a < b[0]:
        print(a - 1 + (b[0] - a)//2 + 1)

    if a > b[1]:
        print(seq[0] - a + (a - b[1])//2 + 1)


