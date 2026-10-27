V = ['a', 'e']
for _ in range(int(input())):
    word_len = int(input())
    word = list(input())
    i = 2
    while i < word_len:
        if word[i] in V:
            word[i - 1] = "." + word[i - 1]
        i += 1
    print(''.join(word))


