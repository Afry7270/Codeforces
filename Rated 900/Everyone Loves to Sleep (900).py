for _ in range(int(input())):
    n, h, m = list(map(int, input().split()))
    alarm = h + m/60
    time_dif = 24
    for i in range(n):
        H, M = list(map(int, input().split()))
        time = H + M/60
        if time >= alarm:
            dif = time - alarm
        else:
            dif = 24 - alarm + time
        if dif <= time_dif:
            time_dif = dif
    print(int(time_dif), round((time_dif-int(time_dif))*60))

