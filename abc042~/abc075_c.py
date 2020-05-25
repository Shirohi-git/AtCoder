from collections import deque


def bfs(NEAR, S, N):
    frag = set([S])
    que = deque([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:
            if i not in frag:
                que.append(i)
                frag.add(i)

    ans = 1
    if len(frag) == N:
        ans = 0
    return ans


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

near = [set([]) for _ in range(n)]
for i, j in ab:
    near[i - 1].add(j - 1)
    near[j - 1].add(i - 1)

cnt = 0
for i, j in ab:
    near[i - 1].remove(j - 1)
    near[j - 1].remove(i - 1)
    cnt += bfs(near,1,n)
    near[i - 1].add(j - 1)
    near[j - 1].add(i - 1)
print(cnt)
