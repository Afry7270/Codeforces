money = int(input())
denominators = [100, 20, 10, 5, 1]
count = 0
i = 0
while money != 0:
    count += (money // denominators[i])
    money = money % denominators[i]
    i = i+1
print(count)

