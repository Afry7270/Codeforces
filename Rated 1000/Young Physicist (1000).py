flag = 0
x_axis = 0
y_axis = 0
z_axis = 0
for _ in range(int(input())):
    x, y, z = list(map(int, input().split()))
    x_axis += x
    y_axis += y
    z_axis += z
if x_axis == 0 and y_axis == 0 and z_axis == 0:
    flag = 1
print(["NO", "YES"][flag == 1])

# Another Solution
# print('YNEOS'[any(map(sum, zip(*[map(int, input().split()) for x in ' '*int(input())])))::2])


