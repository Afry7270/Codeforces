lines = int(input())
for words in range(lines):
    arr = input()
    length = len(arr)
    if length > 10:
        print(f"{arr[0]}{length-2}{arr[-1]}")
    else:
        print(arr)


# for _ in range(int(input())):
#     word = input()
#     le = len(word)
#     print([word, f"{word[0]}{le-2}{word[-1]}"][le > 10])
