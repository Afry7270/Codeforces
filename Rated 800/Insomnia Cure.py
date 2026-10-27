action_seq = [int(input()) for _ in range(4)]
dragon_no = int(input())
unharmed = sum(
    1
    for i in range(1, dragon_no+1)
    if i % action_seq[0] != 0 and i % action_seq[1] != 0 and i % action_seq[2] != 0 and i % action_seq[3] != 0
)

print(dragon_no - unharmed)

# Alternate Solution (Run Time Error)

# action_num = [int(input()) for _ in range(4)]
# dragon_no = int(input())
# arr = []
# num = 1
# i = 1
# j = 0
# while True:
#     while num <= dragon_no:
#         num = i*action_num[j]
#         i += 1
#         if num <= dragon_no:
#             if num not in arr:
#                 arr.append(num)
#     num = 1
#     i = 1
#     j += 1
#     if j > 3:
#         break
# print(len(arr))





