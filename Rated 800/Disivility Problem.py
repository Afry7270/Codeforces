test_cases = int(input())
matrix = [list(map(int, input().split())) for _ in range(test_cases)]
count = 0
i = 0
while i < test_cases:
    if matrix[i][0] % matrix[i][1] != 0:
        print(matrix[i][1]-(matrix[i][0] % matrix[i][1]))
        i += 1
    else:
        print(0)
        i += 1


