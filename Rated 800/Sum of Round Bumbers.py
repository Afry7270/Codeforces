test_cases = int(input())
numbers = [(input()) for _ in range(test_cases)]
for i in range(test_cases):
    listed = list(numbers[i])
    count = 0
    for sig in listed:
        if sig >= '1':
            count += 1
    print(count)
    count = 0
    for j in range(len(listed)):
        if listed[j] >= '1':
            print(listed[j] + (len(listed) - j - 1) * '0', end=' ')
    print("")


