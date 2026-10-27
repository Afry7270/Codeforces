arr = [4, 7, 44, 47, 77, 74, 444, 447, 474, 477, 777, 774, 747]
num = int(input())
flag = 0
for i in range(len(arr)):
    if num % arr[i] == 0:
        flag = 1
        break
print(["NO", "YES"][flag == 1])

# Alternate Solution:
# n=int(input())
# print(["YES","NO"][all(n%i for i in[4, 7, 47, 477])])
