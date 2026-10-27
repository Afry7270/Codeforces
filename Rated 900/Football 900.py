sequence = list(input())
count = 1
store = []
for i in range(0, len(sequence)-1):
    if sequence[i] == sequence[i+1]:
        count += 1
    else:
        if count >= 7:
            break
        else:
            count = 1
if count >= 7:
    print("YES")
else:
    print("NO")




