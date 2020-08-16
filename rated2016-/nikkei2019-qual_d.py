from collections import deque


def topological(N, LIST):  # トポロジカルソート:DAGに適用可
    incnt = [0] * N
    CHILD = [set() for _ in range(N)]
    for a, b in LIST:
        CHILD[a - 1].add(b - 1)
        incnt[b - 1] += 1

    TPLGSORT = []
    que = deque([i for i, num in enumerate(incnt) if num == 0])
    while len(que) > 0:
        q = que.popleft()
        for i in CHILD[q]:
            incnt[i] -= 1
            if incnt[i] == 0:
                que.append(i)
        TPLGSORT.append(q)
    return TPLGSORT, CHILD


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n + m - 1)]

tplg, child = topological(n, ab)
ans = [0] * n
for i in tplg:
    for j in child[i]:
        ans[j] = i + 1
print(*ans, sep='\n')
