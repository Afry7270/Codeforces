test_cases = int(input())
for i in range(test_cases):
    num = list(map(int, input().split()))
    diff = abs(num[0] - num[1])
    if diff > 0 and diff % 10 != 0:
        print(diff//10 + 1)
    elif diff > 0 and diff % 10 == 0:
        print(diff//10)
    else:
        print(0)
