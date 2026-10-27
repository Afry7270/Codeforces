color_seq = (input().split())
no_dup = list(dict.fromkeys(color_seq).keys())
length = len(no_dup)
print(4 - length)