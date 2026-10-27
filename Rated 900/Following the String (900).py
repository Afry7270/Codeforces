for i in range(int(input())):
    arr = [0 for j in range(int(input()))]
    seq = list(map(int, input().split()))
    s = ''
    for k in seq:
        s += chr(arr[k] + 97)
        arr[k] += 1
    print(s)

# Alternate Solution:

# for _ in range(int(input())):
#     n = int(input())
#     res = [97] * (n + 1)
#     arr = list(map(int, input().split()))
#     s = ""
#     for i in range(n):
#         s += chr(res[arr[i]])
#         res[arr[i]] += 1
#     print(s)
