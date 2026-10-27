code = list(input())
length = len(code)
i = 0
while i < length:
    if code[i] == '.':
        print(0, end='')
        i += 1
    elif code[i] == '-' and code[i + 1] == '.':
        print(1, end='')
        i += 2
    elif code[i] == '-' and code[i + 1] == '-':
        print(2, end='')
        i += 2

# Alternate Solution:
# R=str.replace
# print(R(R(R(input(), '--', '2'), '-.', '1'), '.', '0'))

# Or
# print(input().replace("--", "2").replace("-.", "1").replace(".", "0"))
