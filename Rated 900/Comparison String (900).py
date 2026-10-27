for _ in range(int(input())):
    num = int(input())
    seq = list(input())
    maximum = 0
    count = 0
    for i in range(num - 1):
        if seq[i] == seq[i + 1]:
            count += 1
        else:
            count = 0
        if count > maximum:
            maximum = count
    print(maximum + 2)