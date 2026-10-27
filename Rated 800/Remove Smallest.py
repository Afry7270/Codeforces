test_cases = int(input())
for i in range(test_cases):
    length = int(input())
    num = list(map(int, input().split()))
    num.sort()
    if len(num) > 1:
        for k in range(0, len(num) - 1):
            for j in range(0, len(num)-1):
                if abs(num[j] - num[j+1]) == 1 and num[j] < num[j+1]:
                    num.remove(num[j])
                    break
                elif abs(num[j] - num[j+1]) == 1 and num[j] > num[j+1]:
                    num.remove(num[j+1])
                    break
                elif abs(num[j] - num[j+1]) == 0:
                    num.remove(num[j])
                    break
    if len(num) > 1:
        print("NO")
    else:
        print("YES")

