direction = input()
sentence = list(input())
row = "qwertyuiopasdfghjkl;zxcvbnm,./"

for i in range(len(sentence)):
    if direction == "R":
        letter = row.find(sentence[i])
        print(row[letter - 1], end='')
    else:
        letter = row.find(sentence[i])
        print(row[letter + 1], end='')


