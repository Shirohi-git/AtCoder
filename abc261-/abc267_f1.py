def main():
    def nearlist(n0, lst, rev=1):
        res = [[] for _ in range(n0)]
        for a, b in lst:
            res[a - 1].append(b - rev)
            if rev:
                res[b - 1].append(a - 1)
        return res

    def back_dfs(s0, n0):
        flag = [0] * n0
        flag[s0] = 1
        stack = [s0]
        near_it = [iter(ni) for ni in near]

        res = (1, 0)
        while stack:
            q = stack[-1]
            for i in near_it[q]:
                if flag[i]:
                    continue
                flag[i] = 1
                for k in query[i]:
                    if k <= len(stack):
                        dist[(i+1, k)] = stack[-k] + 1
                stack.append(i)
                res = max(res, (len(stack), i))
                break
            else:
                stack.pop()
        return res[1]

    dist = {uki: -1 for uki in UK}
    query = nearlist(N, UK, rev=0)
    near = nearlist(N, AB)
    s = 0
    for _ in range(3):
        s = back_dfs(s, N)
    for uki in UK:
        print(dist[uki])
    return


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    Q = int(input())
    UK = [tuple(map(int, input().split())) for _ in range(Q)]

    main()
