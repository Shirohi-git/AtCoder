def main():

    def dfs(s0, n0):
        dist = [-1] * n0
        dist[s0] = 0
        stack = [s0]

        near_it = [iter(ni) for ni in near]
        while stack:
            q = stack[-1]
            nxt = []
            for i in near_it[q]:
                if dist[i] >= 0:
                    continue
                dist[i] = dist[q] + 1
                nxt.append(i)
                if child[q] == 0:
                    break
                ans[i] = ans[q] - 2 * child[i] + N
            else:
                stack.pop()
                if child[q] == 0:
                    child[q] = sum(child[ni] for ni in near[q]) + 1
            stack += nxt

        if ans[0] == -1:
            ans[0] = sum(dist)
            return dfs(s0, n0)
        return print(*ans, sep='\n')

    near = nearlist(N)
    child, ans = [0] * N, [-1] * N
    return dfs(0, N)


def nearlist(n0):
    NEAR = [[] for _ in range(n0)]
    for a, b in UV:
        NEAR[a - 1].append(b - 1)
        NEAR[b - 1].append(a - 1)
    return NEAR


if __name__ == '__main__':
    N = int(input())
    UV = [list(map(int, input().split())) for _ in range(N-1)]

    main()
