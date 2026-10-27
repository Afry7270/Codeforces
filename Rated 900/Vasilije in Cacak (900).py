for i in range(int(input())):
    n, k, x = list(map(int, input().split()))
    print(["NO", "YES"][(k*(k+1))//2 <= x <= ((2*n - k + 1)*k)//2])
