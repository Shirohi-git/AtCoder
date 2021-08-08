def dfs(s0, n0, near0):
    flag = [0] * n0
    flag[s0] = 1
    stack = [s0]
    res = []

    while stack:
        q = stack[-1]
        res.append(q+1)
        while near0[q]:
            i = near0[q].pop()
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
            break
        else:
            stack.pop()
    return res


def main():

    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in AB:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        res = [sorted(ri)[::-1] for ri in res]
        return res

    near = nearlist(N)
    ans = dfs(0, N, near)

    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    main()
