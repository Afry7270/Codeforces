test_cases = int(input("Test Cases: "))
for cases in range(test_cases):
    arr_length = int(input("Enter array length: "))
    arr_ele = input("Input: ").split()

    product = 1
    for ele in range(arr_length):
        product *= int(arr_ele[ele])

    if product <= 0:
        print(0)

    else:
        print(1)
        print(1, 0)
