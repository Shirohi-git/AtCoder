from itertools import product as pro

n = int(input())
xy = []
for i in range(n):
    a_i = int(input())
    xy.append([tuple(map(int, input().split())) for _ in range(a_i)])

ans = 0
for l in pro([0, 1], repeat=n):
    for i, t in enumerate(l):
        if t == 1:
            if not all(l[x-1] == y for x, y in xy[i]):
                break
    else:
        ans = max(ans, sum(l))

print(ans)
