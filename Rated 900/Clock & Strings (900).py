for i in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    a, b = sorted((a, b))
    c, d = sorted((c, d))
    print(["NO", "YES"][(a < c < b and (d < a or d > b)) or (a < d < b and (c < a or c > b))])

# Another Solution
# if(a<c<b<d or c<a<d<b):print('yes')
