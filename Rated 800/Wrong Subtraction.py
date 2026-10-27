x, y = map(int, (input().split()))
for i in range(y):
    if x % 10 != 0:
        x -= 1
    else:
        x //= 10
print(x)