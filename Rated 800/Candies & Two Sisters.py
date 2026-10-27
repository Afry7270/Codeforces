input_no = int(input())
matrix = [int(input()) for _ in range(input_no)]
for i in range(input_no):
    if matrix[i] % 2 != 0:
        divisions = matrix[i]//2
        print(divisions)
    else:
        divisions = matrix[i]//2 -1
        print(divisions)


