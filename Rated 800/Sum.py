test_cases = int(input())
for i in range(test_cases):
    num = list(map(int, input().split()))
    max_num = max(num)
    num.remove(max_num)
    if max_num == num[0] + num[1]:
        print("YES")
    else:
        print("NO")