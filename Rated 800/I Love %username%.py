contest_no = int(input())
score_seq = list(map(int, input().split()))
min_score = None
max_score = None
count = 0
if contest_no > 1:
    if score_seq[1] > score_seq[0]:
        max_score = score_seq[1]
        min_score = score_seq[0]
    else:
        max_score = score_seq[0]
        min_score = score_seq[1]
    for i in range(2, contest_no):
        if score_seq[i] > max_score:
            count += 1
            max_score = score_seq[i]
        elif score_seq[i] < min_score:
            count += 1
            min_score = score_seq[i]
    if score_seq[0] == score_seq[1]:
        print(count)
    else:
        print(count+1)
else:
    print(0)


# Alternate Solution
# n=int(input())
# l=list(map(int,input().split()))
# c=0
# for i in range(1,n):
# 	g=l[0:i]
# 	m=max(g)
# 	n=min(g)
# 	if l[i]>m or l[i]<n:
# 		c+=1
# print(c)