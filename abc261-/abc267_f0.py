def diameter(s0, n0, near0, goal=None):
    flag = [0] * n0
    flag[s0] = 1
    stack = [s0]
    near_it = [iter(ni) for ni in near0]

    ans = (0, 0)
    while stack:
        q = stack[-1]
        if q == goal:
            return stack
        ans = max(ans, (len(stack), q))
        for i in near_it[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
            break
        else:
            stack.pop()
    return ans[1]


def main():
    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a-1].append(b-1)
            res[b-1].append(a-1)
        return res

    def back_dfs(p):
        while stack:
            q = stack[-1]
            for i in near_it[q]:
                if path[i] != (-1, -1):
                    continue
                path[i] = (len(stack), p)
                record_dist(i)
                stack.append(i)
                break
            else:
                stack.pop()
        return

    def record_dist(v):
        d = 1
        while d <= len(stack):
            d_bra[v].append(stack[-d])
            d <<= 1
        return

    def make_diameter():
        s = diameter(0, N, near)
        t = diameter(s, N, near)
        return diameter(s, N, near, t)

    near = nearlist(N, AB)
    dia = make_diameter()
    d_main = {di: i for i, di in enumerate(dia)}

    near_it = [iter(ni) for ni in near]
    d_bra = [[] for _ in range(N)]
    path = [(-1, -1) for _ in range(N)]
    for di in dia:
        path[di] = (0, di)
    for di in dia:
        stack = [di]
        back_dfs(di)

    for u, k in UK:
        res, u = -1, u-1
        if path[u][0] >= k:
            pow2 = 0
            while k >> pow2:
                if (k >> pow2) & 1:
                    u = d_bra[u][pow2]
                pow2 += 1
            res = u
        else:  # elif path[u][0] > k:
            u, k = path[u][1], k - path[u][0]
            umk, upk = d_main[u] - k, d_main[u] + k
            if 0 <= umk:
                res = dia[umk]
            elif upk < len(dia):
                res = dia[upk]
        print(res+1 if res > -1 else -1)
    return


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    Q = int(input())
    UK = [list(map(int, input().split())) for _ in range(Q)]

    main()
