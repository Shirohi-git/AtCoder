def main():
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
    
        while stack:
            q = stack[-1]
            if q == Y-1:
                return stack
            for i in near_it[q]:
                if flag[i]:
                    continue
                flag[i] = 1
                stack.append(i)
                break
            else:
                stack.pop()
        return
    
    near = nearlist(N, UV)
    ans = back_dfs(X-1, N, near)
    ans = [ai+1 for ai in ans]
    return print(*ans)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(N-1)]

    main()
    