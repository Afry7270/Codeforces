for k in range(int(input())):
    n, m = list(map(int, input().split()))
    flag = 0
    co1 = []
    co2 = []
    for i in range(n):
        row = input()
        if flag == 0:
            if row.count("#") == 1:
                a = row.index("#")
                co1.append(i + 1)
                co1.append(a + 1)
                flag = 1
        elif flag == 1:
            if row.count("#") == 1:
                a = row.index("#")
                co2.append(i + 1)
                co2.append(a + 1)
    if len(co2) > 0:
        print((co1[0]+co2[0])//2, co1[1])
    else:
        print(*co1)

# Alternate Solution 01

# for _ in range(int(input())):
#     h, w = map(int, input().split())
#     grid = []
#     for i in range(h):
#         grid.append(list(input()))
#
#     rows = [grid[i].count('#') for i in range(h)]
#     cols = [[grid[j][i] for j in range(h)].count('#') for i in range(w)]
#
#     ans1 = rows.index(max(rows))
#     ans2 = cols.index(max(cols))
#     print(ans1 + 1, ans2 + 1)


# Alternate Solution 02

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#
#     a = [input().strip() for x in range(n)]
#
#     x, y = [], []
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == "#":
#                 x.append(i)
#                 y.append(j)
#     print((max(x) + min(x)) // 2 + 1, (max(y) + min(y)) // 2 + 1)
