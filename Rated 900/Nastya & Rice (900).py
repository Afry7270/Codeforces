for _ in range(int(input())):
    seq = list(map(int, input().split()))
    if (seq[1]-seq[2])*seq[0] > seq[3]+seq[4] or (seq[1]+seq[2])*seq[0] < seq[3]-seq[4]:
        print("NO")
    else:
        print("YES")
