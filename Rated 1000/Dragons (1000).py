s, n = list(map(int, input().split()))
seq = sorted([list(map(int, input().split())) for _ in range(n)])
flag = 0
for i, j in seq:
    if s > i:
        s = s + j
    else:
        flag = 1
        break
print(["YES", "NO"][flag == 1])


# Alternate Solution
# l = lambda: map(int, input().split())
# a, b = l()
# for i, j in sorted(list(l()) for i in ' ' * b):
#     a = (a + j) * (a > i)
# print('YNEOS'[a < 1::2])
