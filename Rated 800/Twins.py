coin_no = int(input())
coins = list(map(int, input().split()))
coins.sort()
coins.reverse()
total = 0
for i in coins:
    total += i
more_than_half = 0
count = 0
for j in coins:
    more_than_half += j
    count += 1
    if more_than_half > total/2:
        break
print(count)

