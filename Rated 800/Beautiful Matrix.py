# matrix = []
# for i in range(5):
#     row = list(map(int, input().split()))
#     matrix.append(row)


matrix = [list(map(int, input().split())) for _ in range(5)]

r, c = (None, None)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r, c = (i, j)
count = abs(r - 2) + abs(c - 2)
print(count)

# print(matrix)


# kim = [list(input().split()) for _ in range(5)] For string matrix
# kim = [int(input()) for _ in range(5)]
# print(kim)


# Alternate Solution:

# l = [2, 1, 0, 1, 2]
# for i in l:
#     s = input()
#     print(i + l[s.find("1") // 2])
