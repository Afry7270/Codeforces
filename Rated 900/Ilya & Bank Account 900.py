balance = int(input())
if balance >= 0:
    print(balance)
else:
    listed = list(str(balance))
    if balance == -10 or balance == -20 or balance == -30 or balance == -40 or balance == -50 or balance == -60 or balance == -70 or balance == -80 or balance == -90:
        print(0)
    elif len(listed) > 2:
        if listed[-1] > listed[-2]:
            del listed[-1]
        else:
            del listed[-2]
        print("".join(listed))
    else:
        print(0)

# Alternate Solution:
# n = input()
# print(max(map(int, (n, n[:-1], n[:-2]+n[-1]))))
