test_cases = int(input())
for i in range(test_cases):
    seq = list(map(int, input().split()))
    flag = 0
    a = 97
    for j in range(seq[0]):
        print(chr(a), end='')
        a += 1
        if a == 97 + seq[2]:
            a = 97
    print('')


# a = ord('a')
# print(chr(97))

