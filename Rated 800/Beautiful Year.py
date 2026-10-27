year = int(input()) + 1
length = len(str(year))
while True:
    in_list = list(map(int, str(year)))
    no_dup = list(dict.fromkeys(in_list).keys())
    if len(no_dup) != len(in_list):
        year += 1
    else:
        break
print(year)
