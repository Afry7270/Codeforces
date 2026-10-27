# prob_number = int(input())
# count = 0
# for i in range(prob_number):
#     can_solve = input().split()
#     total = 0
#     for j in range(len(can_solve)):
#         total += int(can_solve[j])
#     if total >= 2:
#         count += 1
# print(count)
#

# Alternate Solution
# prob_number = int(input())
# count = 0
# for i in range(prob_number):
#     can_solve = input().split()
#     a, b, c = map(int, can_solve)
#     total = a + b + c
#     if total >= 2:
#         count += 1
# print(count)


for i in range(int(input())):
    num = sum(list(map(int, input().split())))
    print(["NO", "YES"][num >= 2])


