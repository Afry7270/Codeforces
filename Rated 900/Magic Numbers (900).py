seq = input()
seq_test = seq.split("444")
seq_join = ''.join(seq_test)
if len(seq) == len(seq_join):
    seq = seq.split("144")
    seq144 = ''.join(seq)
    seq14 = seq144.split("14")
    seq14 = "".join(seq14)
    seq1 = seq14.split("1")
    final_seq = list(filter(None, seq1))
    print(["NO", "YES"][len(final_seq) == 0])
else:
    print("NO")

# Alternate Solution
# s='144'+input()
# print('YNEOS'[set(s)!=set('14')or'444'in s::2])


# import re
# print('YES' if re.match(r'(14?4?)*$',input()) else 'NO')

