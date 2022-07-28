def dfs(s0, n0, near0):
    dist = [-1] * n0
    dist[s0] = 0
    stack = [s0]

    while stack:
        q = stack.pop()
        dq = dist[q]
        for i, w in near0[q]:
            if dist[i] >= 0:
                continue
            dist[i] = dq ^ w
            stack.append(i)
    return dist


def main():
    def weighted_nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b, w in lst0:
            res[a - 1].append((b - 1, w))
            res[b - 1].append((a - 1, w))
        return res
        
    near = weighted_nearlist(N, ABW)
    dist = dfs(0, N, near)
    
    cnt = [[0] * POW, [0] * POW]
    for di in dist:
        for i in range(POW):
            cnt[(di >> i) & 1][i] += 1
    ans = 0
    for i, c0, c1 in zip(range(POW), *cnt):
        ans += pow(2, i, MOD1) * c0 * c1
        ans %= MOD1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    ABW = [list(map(int, input().split())) for _ in range(N-1)]
    POW = 60
    MOD1 = 10**9 + 7

    main()