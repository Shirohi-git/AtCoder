from itertools import combinations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i, j, k in combinations(range(n), 3):
    a1 = (xy[i][1] - xy[j][1]) * (xy[i][0] - xy[k][0])
    a2 = (xy[i][1] - xy[k][1]) * (xy[i][0] - xy[j][0])
    ans += (a1 == a2)
print('Yes' if ans > 0 else 'No')
