cases_no = int(input())
cases_seq = list(map(int, input().split()))
count = 0
total = 0
for i in range(cases_no):
    total += cases_seq[i]
    if total < 0:
        count += 1
        total = 0
print(count)

