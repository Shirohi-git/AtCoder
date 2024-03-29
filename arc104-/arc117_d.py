import sys
sys.setrecursionlimit(10 ** 7)


def nearlist(N):
    NEAR = [[] for _ in range(N + 1)]
    for a, b in ab:
        NEAR[a - 1].append(b - 1)
        NEAR[b - 1].append(a - 1)
    return NEAR


def bfs(S, N):
    path = [-2] * N
    path[S] = -1
    que = [S]

    for q in que:
        for i in near[q]:
            if path[i] > -2:
                continue
            path[i] = q
            que.append(i)
    return q, path


class Recursive_dfs():
    def __init__(self, S, N):
        self.ans = [0] * N
        self.ans[S] = 1
        self.cnt = 1
        self.idx = -1

    def recdfs(self, p):
        for i in near[p]:
            if i == lst[self.idx]:
                self.idx -= 1
                continue
            if self.ans[i] == 0:
                self.cnt += 1
                self.ans[i] = self.cnt
                self.recdfs(i)
                self.cnt += 1


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

near = nearlist(n)
u, _ = bfs(0, n)
v, p = bfs(u, n)

lst = [-1]
while v > -1:
    lst.append(v)
    near[p[v]].append(v)
    v = p[v]
lst.pop()

rdfs = Recursive_dfs(u, n)
rdfs.recdfs(u)
print(*rdfs.ans)
