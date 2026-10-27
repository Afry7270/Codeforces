magnet_no = int(input())
magnet_seq = [int(input()) for _ in range(magnet_no)]
count = 1
for i in range(0, magnet_no-1):
    if magnet_seq[i] != magnet_seq[i+1]:
        count += 1
print(count)
