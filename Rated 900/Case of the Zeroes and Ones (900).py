input()
num = list(input())
num_zeroes = num.count("0")
num_ones = num.count("1")
if num_zeroes > num_ones:
    print(num_zeroes - num_ones)
else:
    print(num_ones - num_zeroes)


