statement_no = int(input())
x = 0
for i in range(statement_no):
    statement = (input())
    if "+" in statement:
        x += 1
    else:
        x -= 1
print(x)