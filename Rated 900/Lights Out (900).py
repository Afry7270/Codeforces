matrix = [list(map(int, input().split())) for _ in range(3)]
toggle = [[1, 1, 1] for _ in range(3)]
for i in range(3):
    for j in range(3):
        if matrix[i][j] % 2 != 0:
            if toggle[i][j] == 0:
                toggle[i][j] = 1
            else:
                toggle[i][j] = 0
            if 1 <= i <= 2 and 0 <= j <= 2:
                if toggle[i - 1][j] == 0:
                    toggle[i - 1][j] = 1
                else:
                    toggle[i - 1][j] = 0
            if 0 <= i <= 1 and 0 <= j <= 2:
                if toggle[i + 1][j] == 0:
                    toggle[i + 1][j] = 1
                else:
                    toggle[i + 1][j] = 0
            if 0 <= i <= 2 and 0 <= j <= 1:
                if toggle[i][j + 1] == 0:
                    toggle[i][j + 1] = 1
                else:
                    toggle[i][j + 1] = 0
            if 0 <= i <= 2 and 1 <= j <= 2:
                if toggle[i][j - 1] == 0:
                    toggle[i][j - 1] = 1
                else:
                    toggle[i][j - 1] = 0
for i in range(3):
    for j in range(3):
        print(toggle[i][j], end="")
    print("")





