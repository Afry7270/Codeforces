for _ in range(int(input())):
    n, f, a, b = list(map(int, input().split()))
    moments = list(map(int, input().split()))
    new_moments = [0] + moments
    charge = f
    flag = 0
    for i in range(n):
        if a*(new_moments[i + 1] - new_moments[i]) > b:
            charge = charge - b
        else:
            charge = charge - a*(new_moments[i + 1] - new_moments[i])
        if charge <= 0:
            flag = 1
            break
    print(['YES', 'NO'][flag == 1])
