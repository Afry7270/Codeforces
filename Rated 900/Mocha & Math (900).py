for i in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    result = seq[0]
    for j in seq:
        result = j & result
    print(result)
