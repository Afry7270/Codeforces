bact = int(input())
i = 0
flag = 0
while True:
    while True:
        if 2**i > bact:
            bact = bact - 2 ** (i - 1)
            i = i - 1
            flag += 1
            break
        elif 2**i == bact:
            bact = bact - 2 ** i
            flag += 1
            break
        else:
            i += 1
    i = 0
    if bact == 0:
        break
print(flag)
