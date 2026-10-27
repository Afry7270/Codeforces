for i in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    count = 0
    temp = []
    for j in s:
        if j not in temp:
            temp.append(j)
            if s.count(j) % 2 != 0:
                count += 1
    print(["NO","YES"][k >= count - 1])
