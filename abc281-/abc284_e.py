def nearlist(n0, lst0):
    res = [[] for _ in range(n0)]
    for a, b in lst0:
        res[a-1].append(b-1)
        res[b-1].append(a-1)
    return res


def back_dfs(s0, n0, near0):
    flag = [0] * n0
    flag[s0] = 1
    stack = [s0]
    near_it = [iter(ni) for ni in near0]
    
    res = 1
    while stack:
        q = stack[-1]
        for i in near_it[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
            res += 1
            break
        else:
            p = stack.pop()
            flag[p] = 0
            near_it[p] = iter(near0[p])
        if res >= INF:
            return INF
    return res


def main():
    near = nearlist(N, UV)
    ans = back_dfs(0, N, near)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**6

    main()