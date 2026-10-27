for i in range(int(input())):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr_sum = [0]
    for j in range(n):
        arr_sum.append(arr_sum[-1] + arr[j])
    for _ in range(q):
        l, r, k = list(map(int, input().split()))
        total = arr_sum[-1] + (k*(r - l + 1) - (arr_sum[r] - arr_sum[l - 1]))
        print(["YES", "NO"][total % 2 == 0])


# WORKS but RUNTIME ERROR

# for i in range(int(input())):

#     n, q = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     saved = tuple(arr)
#     for j in range(q):
#         l, k, r = list(map(int, input().split()))
#         for p in range(l-1, k):
#             arr[p] = r
#         print(["YES", "NO"][sum(arr) % 2 == 0])
#         arr = list(saved)

# Alternate Solution:
# for _ in range(int(input())):
#     n, q = map(int, input().split())
#     a = list(map(int, input().split()))
#     S = [0]
#     for i in a:
#         S.append(S[-1] + i)
#     for _ in range(q):
#         l, r, k = map(int, input().split())
#         s = S[l - 1] + (r - l + 1) * k + (S[-1] - S[r])
#         print('YES' if s % 2 else 'NO')
