word = list(input())
reverse = input()
copy = word.copy()
copy.reverse()
new = ''.join(copy)
if new == reverse:
    print("YES")
else:
    print("NO")
