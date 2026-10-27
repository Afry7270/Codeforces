# test_cases = int(input())
# for i in range(test_cases):
#     num = int(input())
#     flag = 0
#     for j in range(1, 50):
#         guess = 2**j
#         if guess == num:
#             print("NO")
#             flag = 1
#             break
#     if flag == 0:
#         print("YES")

# # Alternate Solution:
for _ in range(int(input())):
    n = int(input())
    print('YNEOS'[n & (n-1) < 1::2])



