seq = list(map(int, input().split()))
total = seq[0]
i = 1
while seq[1] * i <= seq[0]:
    seq[0] += 1
    i += 1
print(seq[0])


# Alternate Solution:
# a,b=map(int,input().split());print((a-1)//(b-1)+a)

