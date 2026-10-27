numbers = list(map(int, input().split()))
max_num = max(numbers)
numbers.remove(max_num)
a = max_num - numbers[0]
b = max_num - numbers[1]
c = max_num - numbers[2]
print(a, b, c)