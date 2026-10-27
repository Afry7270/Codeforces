people_no = int(input())
opinions = list(map(int, input().split()))
count = 0
for i in range(people_no):
    if opinions[i] == 1:
        count = 1
if count == 0:
    print("EASY")
else:
    print("HARD")
