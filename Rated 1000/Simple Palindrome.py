arr = "aeiou"
for _ in range(int(input())):
    num = int(input())
    word = []
    j = 0
    for i in range(num):
        word.append(arr[j])
        j += 1
        if j == 5:
            j = 0
    print(''.join(sorted(word)))
