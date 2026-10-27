# total_axes = int(input())
# seq = list(map(int, input().split()))
# store = []
# if total_axes > 2:
#     store.append(abs(seq[0] - seq[1]))
#     store.append(abs(seq[0] - seq[-1]))
#     print(*store)
#     store = []
#     for i in range(1, total_axes - 1):
#         store.append(min(abs(seq[i] - seq[i - 1]), abs(seq[i] - seq[i + 1])))
#         store.append(max(abs(seq[i] - seq[0]), abs(seq[i] - seq[-1])))
#         print(*store)
#         store = []
#     store.append(abs(seq[-1] - seq[-2]))
#     store.append(abs(seq[0] - seq[-1]))
#     print(*store)
# else:
#     store.append(abs(seq[0] - seq[-1]))
#     store = store * 2
#     print(*store)
#     print(*store)

# Alternate Solution
n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    t = x[i]
    print(min(abs(t-x[i-1]), abs(x[i-n+1]-t)), max(t-x[0], x[n-1]-t))
