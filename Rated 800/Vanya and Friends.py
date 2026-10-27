n, h_fence = map(int, input().split())
h_friends = list(map(int, input().split()))
count = 0
for i in range(n):
    if h_friends[i] > h_fence:
        count += 2
    else:
        count += 1
print(count)
print(h_friends)
