coordinate = int(input())
steps = coordinate//5
remainder = coordinate % 5
if remainder == 0:
    total = steps
else:
    total = steps + 1
print(total)
