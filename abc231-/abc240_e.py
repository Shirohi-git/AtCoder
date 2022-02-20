def back_dfs(s0, n0, near0):
    flag = [0] * n0
    flag[s0] = 1

    stack = [s0]
    near_it = [iter(ni) for ni in near0]

    mx = 0
    res = [None] * N
    while stack:
        q = stack[-1]
        for i in near_it[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
            break
        else:
            l, r = mx+1, mx
            for i in near0[q]:
                if res[i]:
                    l = min(res[i][0], l)
                    r = max(res[i][1], r)
            res[q] = [l, max(r, l)]
            mx = max(r, l)
            stack.pop()
    return res


def main():
    def nearlist(n0, lst0):  # 隣接リスト
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, UV)
    ans = back_dfs(0, N, near)
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N = int(input())
    UV = [list(map(int, input().split())) for _ in range(N-1)]

    main()
