k = int(input())
growth = list(map(int, input().split()))
sorted_growth = sorted(growth, reverse=True)
flag = 0
total = 0
for i in range(12):
    if total >= k:
        break
    else:
        total += sorted_growth[i]
    flag += 1
print([flag, -1][total < k])


# Alternate Solution
# k = int(input())
# a = sorted([*map(int, input().split())])
# i = 11
# while k > 0 and i > -1:
#     k -= a[i]
#     i -= 1
# print([11-i, -1][k > 0])

