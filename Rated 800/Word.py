word = list(input())
upper = 0
lower = 0
for i in word:
    if 'A' <= i <= 'Z':
        upper += 1
    else:
        lower += 1
if lower >= upper:
    print(''.join(word).lower())
else:
    print(''.join(word).upper())