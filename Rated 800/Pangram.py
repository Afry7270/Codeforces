# alphabet_upper = []
# alphabet_lower = []
# for i in range(65, 91):
#     alphabet_upper.append(chr(i))
# for i in range(97, 123):
#     alphabet_lower.append(chr(i))
# print(alphabet_lower)

alphabet_no = int(input())
string = input()
upper_string = list(string.upper())

no_dup = list(dict.fromkeys(upper_string).keys())
no_dup.sort()
if len(no_dup) == 26:
    print("YES")
else:
    print("NO")
