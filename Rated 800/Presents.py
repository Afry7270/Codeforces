people_no = int(input())
gift_seq = list(map(int, input().split()))
for i in range(people_no):
    index = gift_seq.index(i+1)
    print(index + 1, end=' ')
