first_num = list(input())
second_num = list(input())
output = []
for i in range(len(first_num)):
    if first_num[i] == second_num[i]:
        output.append('0')
    else:
        output.append('1')
print(''.join(output))

