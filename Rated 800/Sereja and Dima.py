# test_cases = int(input())
# card_list = list(map(int, input().split()))
# sereja = []
# dima = []
# exchange = 1
# for i in range(test_cases):
#     if exchange == 1:
#         if card_list[0] > card_list[-1]:
#             sereja.append(card_list[0])
#             card_list.remove(card_list[0])
#         else:
#             sereja.append(card_list[-1])
#             card_list.remove(card_list[-1])
#
#     elif exchange == -1:
#         if card_list[0] > card_list[-1]:
#             dima.append(card_list[0])
#             card_list.remove(card_list[0])
#         else:
#             dima.append(card_list[-1])
#             card_list.remove(card_list[-1])
#     exchange = exchange*(-1)
#
# print(sum(sereja), sum(dima))

#Alternate Solution:
x = [0, 0]
n, a = int(input()), list(map(int, input().split()))
for i in range(n):
    b = max(a[0], a[-1])
    x[i % 2] += b
    a.remove(b)
print(*x)
