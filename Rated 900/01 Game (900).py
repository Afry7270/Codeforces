# test_cases = int(input())
# for i in range(test_cases):
#     seq = input()
#     length = len(seq)
#     flag = 0
#     while True:
#         split_01 = list(filter(None, seq.split("01", 1)))
#         new_seq = "".join(split_01)
#         if len(seq) != len(new_seq):
#             length = len(new_seq)
#             seq = new_seq
#             flag += 1
#             continue
#         else:
#             split_10 = list(filter(None, seq.split("10", 1)))
#             new_seq = "".join(split_10)
#             if len(seq) != len(new_seq):
#                 length = len(new_seq)
#                 seq = new_seq
#                 flag += 1
#                 continue
#
#         if len(new_seq) == 0 or length == len(new_seq):
#             break
#     print(["NET", "DA"][flag % 2 != 0])


# Alternate Solution
# for _ in range(int(input())):
#     s = input()
#     print(('NET', 'DA')[min(s.count('0'), s.count('1')) % 2])

