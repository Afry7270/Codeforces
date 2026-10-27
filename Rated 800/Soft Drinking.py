import math
sequence = list(map(int, input().split()))
drink = (sequence[1]*sequence[2])/sequence[6]
slices = sequence[3]*sequence[4]
salt = sequence[5]/sequence[7]
arr = [drink, slices, salt]
print(math.floor(min(arr)//sequence[0]))
