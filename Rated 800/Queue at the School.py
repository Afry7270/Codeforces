n, time = map(int, input().split())
sequence = list(input())

for t in range(time):
    i = 0
    count = 0
    while i < n-1:
        if sequence[i] == 'B' and sequence[i + 1] == 'G':
            sequence[i] = 'G'
            sequence[i+1] = 'B'
            i += 2
            count += 1
        else:
            i += 1

print(''.join(sequence))
