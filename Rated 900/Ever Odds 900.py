seq = list(map(int, input().split()))
if seq[0] % 2 != 0:
    if seq[1] > seq[0]//2 + 1:
        print((seq[1] - (seq[0]//2 + 1))*2)
    else:
        print(seq[1]*2 - 1)
else:
    if seq[1] > seq[0]//2:
        print((seq[1] - seq[0]//2)*2)
    else:
        print(seq[1]*2 - 1)