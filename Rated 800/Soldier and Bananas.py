arr = input().split()
price = int(arr[0])
money = int(arr[1])
count = int(arr[2])
total = 0
for i in range(1, count+1):
    total += i*price
borrow = total - money
if borrow >= 0:
    print(borrow)
else:
    print(0)


# Alternate Solution

# k,n,w=map(int,input().split())
# print(max(0,k*w*-~w//2-n))
#
# k,n,w=map(int,input().split())
# print(max(0,k*w*(w+1)//2-n))


