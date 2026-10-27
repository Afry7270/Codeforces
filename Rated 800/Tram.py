stops = int(input())
passengers = [list(map(int, input().split())) for i in range(stops)]
outside = []
inside = []
total = 0
min_cap = 0
for i in range(stops):
    outside.append(passengers[i][0])
    inside.append(passengers[i][1])

for j in range(stops):
    total = total - outside[j] + inside[j]
    if total > min_cap:
        min_cap = total

# Alternate:
# for i in passengers:
#     total = total - i[0] + i[1]
#     if total > min_cap:
#         min_cap = total

print(min_cap)
