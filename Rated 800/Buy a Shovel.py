price_coin = list(map(int, input().split()))
temp = price_coin[0]
price = price_coin[0]
special_coin = price_coin[1]
count = 1
while True:
    if price % 10 == 0:
        break
    elif price % 10 != 0 and (price % 10 - special_coin) == 0:
        break
    else:
        price = price + temp
        count += 1
print(count)
