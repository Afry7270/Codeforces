input_seq = list(map(int, input().split()))
fox = input_seq[1]*"#"
snake_list = list((input_seq[1] - 1) * "." + "#")
snake = ''.join(snake_list)
snake_rev_list = snake_list.copy()
snake_rev_list.reverse()
snake_rev = ''.join(snake_rev_list)

count = 0
for i in range(input_seq[0]):
    if i % 2 == 0:
        print(fox)
    elif count == 0:
        print(snake)
        count = 1
    elif count == 1:
        print(snake_rev)
        count = 0


