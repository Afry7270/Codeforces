# word = "hello"
# string = input()
# j = 0
# for i in range(len(string)):
#     if string[i] == word[j]:
#         j += 1
#     if j == 5:
#         break
# print(["NO", "YES"][j == 5])

# Alternate Solution
s = iter(input())
print('NYOE S'[all(c in s for c in 'hello')::2])
