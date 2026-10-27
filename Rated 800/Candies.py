test_cases = int(input())
for i in range(test_cases):
    num = int(input())
    total = 3
    count = 2
    while num % total:
        count = count * 2
        total = total + count
    print(num // total)


# Alternate Solution
# for _ in range(int(input())):
#     n = int(input())
#     k = 3
#     while n % k:
#         k = k * 2 + 1
#     print(n // k)

