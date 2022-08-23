def main():
    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def bfs(s0):
        res = 0
        que = [s0]
        for q in que:
            for i in near[q]:
                if elec[i]:
                    continue
                elec[i] = 1
                res += 1
                que.append(i)
            near[q] = []
        return res

    x_set = set(X)
    uv = [UV[i] for i in range(E) if i+1 not in x_set]

    cnt = 0
    near = nearlist(N+M, uv)
    elec = [0] * N + [1] * M
    for i in range(N, N+M):
        cnt += bfs(i)

    ans = [cnt]
    for xi in X[1:][::-1]:
        u, v = UV[xi-1]
        if elec[u-1] & elec[v-1] == 0:
            near[u-1].append(v-1)
            near[v-1].append(u-1)
        if elec[u-1] ^ elec[v-1] == 1:
            cnt += bfs(u-1 if elec[u-1] else v-1)
        ans.append(cnt)
    return print(*ans[::-1], sep='\n')


if __name__ == '__main__':
    N, M, E = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(E)]
    Q = int(input())
    X = [int(input()) for _ in range(Q)]

    main()
