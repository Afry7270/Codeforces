test_cases = int(input())
for i in range(test_cases):
    num = int(input())
    flag = 0
    neg = 0
    while num != 1:
        if num % 3 != 0:
            neg = 1
            break
        else:
            if num % 6 == 0:
                num = num // 6
                flag += 1
            else:
                num = num * 2
                flag += 1
    if neg == 1:
        print(-1)
    else:
        print(flag)



