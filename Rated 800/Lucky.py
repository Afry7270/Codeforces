test_cases = int(input())
for i in range(test_cases):
    ticket = list(map(int, input()))
    if ticket[0] + ticket[1] + ticket[2] == ticket[3] + ticket[4] + ticket[5]:
        print("YES")
    else:
        print("NO")


