n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]

near = [set([]) for _ in range(n)]
for a, b in ab:
    near[a - 1].add(b - 1)
    near[b - 1].add(a - 1)

for i in near[0]:
    if i in near[n - 1]:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')
