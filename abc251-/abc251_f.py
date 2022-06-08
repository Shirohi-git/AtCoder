def bfs(s0, n0, near0):
    flag = [0] * n0
    flag[s0] = 1
    que = [s0]

    res = []
    for q in que:
        for i in near0[q]:
            if flag[i]:
                continue
            flag[i] = 1
            que.append(i)
            res.append((q, i))
    return res


def dfs(s0, n0, near0):
    flag = [0] * n0
    flag[s0] = 1
    stack = [s0]
    near_it = [iter(ni) for ni in near0]

    res = []
    while stack:
        q = stack[-1]
        for i in near_it[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
            res.append((q, i))
            break
        else:
            stack.pop()
    return res


def main():

    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, UV)
    ans = dfs(0, N, near) + bfs(0, N, near)
    for a, b in ans:
        print(a+1, b+1)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]

    main()
