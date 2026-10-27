team_no = int(input())
uni_matrix = [list(map(int, input().split())) for _ in range(team_no)]
home = []
away = []
count = 0
# for i in range(team_no):
#     home.append(uni_matrix[i][0])
# for i in range(team_no):
#     away.append(uni_matrix[i][1])
# for i in home:
#     for j in away:
#         if i == j:
#             count += 1
for i in range(team_no):
    for j in range(team_no):
        if uni_matrix[i][0] == uni_matrix[j][1]:
            count += 1
print(count)

