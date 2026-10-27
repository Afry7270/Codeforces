drink_no = int(input())
orange_juice = list(map(int, input().split()))
total = 0
for i in orange_juice:
    total += i
percentage = total/(drink_no*100)
print(percentage*100)