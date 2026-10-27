n, m, a = list(map(int, input().split()))
x = n // a if n % a == 0 else n // a + 1
y = m // a if m % a == 0 else m // a + 1
if x == 0:
    x = 1
if y == 0:
    y = 1
print(x * y)

# Alternate Solution
# n,m,a=map(int,input().split())
# print(-n//a*(-m//a))
