# statement = list(input())
# flag = 0
# for i in range(len(statement)):
#     if statement[i] == 'H' or statement[i] == 'Q' or statement[i] == '9':
#         flag = 1
#         break
# if flag == 1:
#     print('YES')
# else:
#     print('NO')

# Alternate Solution:
print('YES'if{*'HQ9'} & {*input()}else'NO')
