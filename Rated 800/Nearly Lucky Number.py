number = list(map(int, (input())))
count = 0
for i in range(len(number)):
    if number[i] == 4 or number[i] == 7:
        count += 1
    else:
        count += 0
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
