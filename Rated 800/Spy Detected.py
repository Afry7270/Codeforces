# test_cases = int(input())
#
# for i in range(test_cases):
#     arr = []
#     count = int(input())
#     numbers = list(map(int, input().split()))
#     for j in range(count):
#         for k in range(j+1, count):
#             if numbers[j] == numbers[k]:
#                 arr.append(numbers[k])
#
#     unique = set(list(dict.fromkeys(numbers).keys()))
#     dup = set(arr)
#     single = list(unique ^ dup)
#     print(numbers.index(single[0])+1)


# Alternate
for _ in range(int(input())):
    input()
    s = input().split()
    print(s.index(min(s, key=s.count)) + 1)

