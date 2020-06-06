n, m, q = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(q)]

near = [[] for _ in range(n)]
for i, j in uv:
    near[i - 1].append(j - 1)
    near[j - 1].append(i - 1)

for l in s:
    print(c[l[1]-1])
    if len(l) == 2:
        for i in near[l[1] - 1]:
            c[i] = c[l[1]-1]
    if len(l) == 3:
        c[l[1] - 1] = l[2]
