from math import gcd

for i in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    total = 0
    even = []
    odd = []
    odd.sort()
    for j in range(n):
        even.append(seq[j]) if seq[j] % 2 == 0 else odd.append(seq[j])
    for k in range(len(even)):
        total += n - 1
        n -= 1
    p = 1
    for l in range(len(odd)):
        for m in range(p, len(odd)):
            if gcd(odd[l], 2 * odd[m]) > 1:
                total += 1
        p += 1
    print(total)

# Alternate Solution

# from math import gcd
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(len([i for i in range(n) for j in range(i + 1, n) if gcd(a[i], 2 * a[j]) > 1 or gcd(2 * a[i], a[j]) > 1]))
