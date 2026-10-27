for i in range(int(input())):
    matrix = [*(input() for j in range(9))]
    print(["B", "R"]["RRRRRRRR" in matrix])



# for n in range(int(input())):
#     print("BR"[any([*(input() == "RRRRRRRR"for i in range(9))])])
