def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in ab:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(S, N):
    ans, flag = [-1] * N, [0] * N
    ans[S], flag[S] = c.pop(), 1
    que = [S]

    for q in que:
        for i in near[q]:
            if flag[i]:
                continue
            ans[i], flag[i] = c.pop(), 1
            que.append(i)
    return ans


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
c = sorted(map(int, input().split()))

near = nearlist(n)
print(sum(c) - max(c))
print(*bfs(0, n))
