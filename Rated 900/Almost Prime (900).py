num = int(input())
temp = 0
for n in range(1, num + 1):
    arr = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                arr.append(i)
    if len(arr) == 2:
        temp += 1
print(temp)

