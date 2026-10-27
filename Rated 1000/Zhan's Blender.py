import math
for _ in range(int(input())):
    fruits = int(input())
    x, y = list(map(int, input().split()))
    print(math.ceil(fruits/(min(x, y))))
