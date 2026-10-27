for i in range(int(input())):
    input()
    s = input()
    s = s.replace("map", '0')
    s = s.replace('pie', '0')
    print(s.count('0'))


# Alternate Solution
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(s.count('pie')+s.count('map')-s.count('mapie'))