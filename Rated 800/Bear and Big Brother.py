weight = list(map(int, input().split()))
limak = weight[0]
bob = weight[1]
count = 0
while True:
    limak = limak*3
    bob = bob*2
    count += 1
    if limak > bob:
        break
print(count)