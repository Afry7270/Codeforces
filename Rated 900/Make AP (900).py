test_cases = int(input())
for i in range(test_cases):
    a, b, c = list(map(int, input().split()))
    print(["NO", "YES"][2*b > c and (2*b-c) % a == 0 or 2*b > a and (2*b-a) % c == 0 or (c+a) % (2*b) == 0])

