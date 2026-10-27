# letters = list(input())
# letters.remove(letters[0])
# letters.remove(letters[-1])
# length = len(letters)
# new_letters = []
# for i in range(0, length, 3):
#     new_letters.append(letters[i])
# no_dup = list(dict.fromkeys(new_letters).keys())
# print(len(no_dup))

# Alternate Solution
letters = (input())
no_dup = set(letters+', ')
print(len(no_dup)-4)


# print(len(set(i for i in input()[1:-1].split(", ") if i)))

# print(len((set(input()+', ')))-4)






