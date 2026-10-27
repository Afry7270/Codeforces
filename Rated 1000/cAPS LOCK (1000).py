word = input()
if len(word) == 1:
    print(word.swapcase())
elif word == word.upper():
    print(word.lower())
elif word[0].islower() and word[1:].isupper():
    print(word.title())
else: print(word)
