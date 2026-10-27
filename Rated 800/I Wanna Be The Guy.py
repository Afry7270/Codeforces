levels = int(input())
little_x = list(map(int, input().split()))
little_y = list(map(int, input().split()))
arr = []
# sorted_arr = []
for i in range(1, len(little_x)):
    if little_x[i] not in arr:
        arr.append(little_x[i])
for j in range(1, len(little_y)):
    if little_y[j] not in arr:
        arr.append(little_y[j])
if len(arr) == levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")


# for k in range(1, levels+1):
#     sorted_arr.append(k)
# if arr.sort() == sorted_arr:
#     print()