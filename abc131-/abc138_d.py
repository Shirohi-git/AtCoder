import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

n, q = map(int, input().split())

edge = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    edge[a-1].append(b)
    edge[b-1].append(a)

cnt = [0 for _ in range(n)]
for i in range(q):
    p, x = map(int, input().split())
    cnt[p-1] += x


def dfs(now, bef):
    for nxt in edge[now-1]:
        if nxt != bef:
            cnt[nxt-1] += cnt[now-1]
            dfs(nxt, now)


dfs(1, -1)
print(*cnt)
