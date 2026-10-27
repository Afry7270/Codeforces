seq = list(map(int, input().split()))
prices = list(map(int, input().split()))
total = 0
for i in range(seq[1]):
    if min(prices) < 0:
        total += min(prices)
        prices.remove(min(prices))
print(abs(total))