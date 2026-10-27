# test_cases = int(input())
# for i in range(test_cases):
#     arr = []
#     length = int(input())
#     for j in range(1, length + 1):
#         arr.append(j)
#     if length == 1:
#         print(1)
#     else:
#         num = 0
#         for k in range(3):
#
#             divider = 1
#             for m in range(2, arr[num+1]):
#                 if arr[num + 1] % m == 0:
#                     divider = m
#                 if arr[num + 1] == 2:
#                     divider = 1
#             arr[arr.index(num + 2)], arr[divider - 1] = arr[divider - 1], arr[arr.index(num + 2)]
#             num += 1
#         print(arr.index(1)+1)

# Alternate Solution 01
import math
# for _ in range(int(input())):
#     n = bin(int(input()))[3:]
#     print(2**len(n))

# # Alternate Solution 02
# for _ in range(int(input())):
#     n = int(input())
#     print(1<<n.bit_length()-1)

# Alternate Solution 03
# import math
# t = int(input())
# for i in range(t):
#     n=int(input())
#     print(2**int(math.log2(n)))
num = 5
bina = 1<<num.bit_length()
print(bina)