def main():

    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def bfs(res=[1]):
        stack = [0]
        while stack:
            q = stack.pop()
            flag[q] = 1
            for p in near[q]:
                if not flag[p]:
                    stack.append(p), res.append(p+1)
                    break
        return res[::-1]

    flag = [0] * N
    near = nearlist(N, AB)
    ans = dfs(dfs())
    return print(len(ans)), print(*ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]

    main()
