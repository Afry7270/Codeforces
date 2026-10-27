guest = list(input())
host = list(input())
fallen = list(input())
fallen.sort()
new = guest + host
new.sort()

if fallen == new:
    print("YES")
else:
    print("NO")