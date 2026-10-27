x, y = list(map(int, input().split()))
area = x * y
if area % 2 == 0:
    print(area//2)
else:
    print((area-1)//2)