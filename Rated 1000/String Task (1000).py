# import re
# string = input().lower()
# new_string = re.split(pattern=r'[aeiouy]',
#                       string=string)
# string = list(''.join(list(filter(None, new_string))))
# for i in range(len(string)):
#     string[i] = "." + string[i]
# print(''.join(string))


# Alternate Solution:
# [print(end='.'+c)for c in input().lower()if~-(c in'aeiouy')]


# Alternate Solution 02
# string = input().lower()
# for i in string:
#     if i not in "aeiouy":
#         print('.' + i, end='')
