socks = list(map(int, input().split()))
print(min(socks), end=' ')
print((max(socks) - min(socks))//2)