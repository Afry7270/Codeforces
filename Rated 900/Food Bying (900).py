for _ in range(int(input())):
    store = int(input())
    num = store
    while True:
        quotient = store // 10
        num += quotient
        if quotient > 0:
            store = quotient + (store % 10)
        else:
            break
    print(num)

# Alternate Solution
# for _ in range(int(input())):
#     n=int(input())
#     print(int(n // 0.9))
