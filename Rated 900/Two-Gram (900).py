num = int(input())
seq = list(input())
max_flag = 0
char = [seq[0], seq[1]]
if num >= 3:
    for i in range(num - 2):
        flag = 0
        for j in range(num - 2):
            if seq[i] == seq[j + 1] and seq[i + 1] == seq[j + 2]:
                flag += 1
        if flag > max_flag:
            max_flag = flag
            char[0] = seq[i]
            char[1] = seq[i + 1]
    print("".join(char))
else:
    print(''.join(seq))

# Alternate Solution
# i = input()
# a = input()
# b = [*zip(a, a[1:])]
# print(''.join(max(b, key=b.count)))



