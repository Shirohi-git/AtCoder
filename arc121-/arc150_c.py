def main():
    def nearlist(n0, lst):
        res = [[] for _ in range(n0)]
        for a, b in lst:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def que_bfs(s0, n0, near0):
        from collections import deque

        dist = [-2] * n0
        dist[s0] = (B[0] == A[0]) - 1
        que = deque([s0])

        while que:
            q = que.popleft()
            dq = dist[q]
            for i in near0[q]:
                if dist[i] > -2:
                    continue
                if dq+1 < K and B[dq+1] == A[i]:
                    dist[i] = dq + 1
                    que.append(i)
                else:  # elif dq+1 >= K or B[dq+1] != A[i]:
                    dist[i] = dq
                    que.appendleft(i)
        return dist

    near = nearlist(N, UV)
    dist = que_bfs(0, N, near)
    return print('Yes' if dist[-1] == K-1 else 'No')


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
