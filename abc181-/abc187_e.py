def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in ab:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def depth(N):
    flag, dist = [1] + [0] * N, [0] + [-1] * N
    que = [0]

    for q in que:
        for i in near[q]:
            if not flag[i]:
                flag[i], dist[i] = 1, dist[q] + 1
                que.append(i)
    return que, dist


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
q = int(input())
tex = [list(map(int, input().split())) for _ in range(q)]

near = nearlist(n)
(que, dep), cnt = depth(n), [0] * n
for ti, ei, xi in tex:
    a, b = ab[ei - 1]
    a, b, ti = a - 1, b - 1, ti - 1
    if dep[a] > dep[b]:
        a, b, ti = b, a, ti ^ 1
    cnt[0] += (1 - ti) * xi
    cnt[b] += (2 * ti - 1) * xi

for q in que:
    for i in near[q]:
        if dep[i] > dep[q]:
            cnt[i] += cnt[q]
print(*cnt, sep='\n')
