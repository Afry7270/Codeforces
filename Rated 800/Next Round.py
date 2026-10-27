x, y = map(int, input().split())
scores = (input()).split()
count = 0
for i in range(x):
    if int(scores[i]) >= int(scores[y-1]) and int(scores[i]) > 0:
        count += 1
print(count)
