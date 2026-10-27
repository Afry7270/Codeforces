math = list(input())

count_1, count_2, count_3 = (math.count('1'), math.count('2'), math.count('3'))
for i in range(0, len(math), 2):
    if i <= (count_1*2)-1:
        math[i] = '1'
    elif (count_1*2)-1 < i <= ((count_1 + count_2)*2)-1:
        math[i] = '2'
    elif (count_1 + count_2)*2 - 1 < i <= len(math):
        math[i] = '3'
sorted_math = ''.join(math)
print(sorted_math)


# Alternate Solution:
# math = input().split('+')
# math.sort()
# print('+'.join(math))


