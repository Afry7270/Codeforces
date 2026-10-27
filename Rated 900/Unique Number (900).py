test_cases = int(input())
for i in range(test_cases):
    num = int(input())
    n = 9
    total = 9
    arr = [9]
    while True:
        if 9 < num <= 45:
            m = num - total
            n -= 1
            if m > n:
                arr.append(n)
                total += n
            else:
                arr.append(m)
                arr.reverse()
                print(''.join(map(str, arr)))

                break
        elif num > 45:
            print(-1)
            break
        else:
            print(num)
            break
