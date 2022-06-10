import sys
input = sys.stdin.readline


h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

xy = {}
for x, ai in enumerate(a):
    for y, aij in enumerate(ai):
        xy[aij] = (x, y)

acc = [[0] for _ in range(d)]
for num in range(d + 1, h * w + 1):
    (x, y), (i, j) = xy[num - d], xy[num]
    cost = abs(x - i) + abs(y - j)
    acc[num % d].append(acc[num % d][-1] + cost)

for l, r in lr:
    ans = acc[r % d][(r - 1) // d] - acc[l % d][(l - 1) // d]
    print(ans)
