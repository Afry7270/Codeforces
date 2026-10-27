a = []
seq = [input() for i in range(int(input()))]

string = None
for i in seq:
    goals = list(i)
    unique = sorted(list(dict.fromkeys(goals).keys()))
    counts = dict()
    for j in goals:
        counts[j] = counts.get(j, 0) + 1
    a.append(max(counts, key=counts.get))
print(max(a))


