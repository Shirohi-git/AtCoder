class Dinic():
    def __init__(self, n0):
        self.N, self.INF = n0, 10**10
        self.edge_cnt = 0
        self.edge = []
        self.near_edge = [[] for _ in range(n0)]

    def add__edge(self, v1, v2, cap1, cap2=0):
        self.edge += [[v2, cap1], [v1, cap2]]
        self.near_edge[v1].append(self.edge_cnt)
        self.near_edge[v2].append(self.edge_cnt + 1)
        self.edge_cnt += 2

    def is_connect(self, s, t):
        self.level = level = [-1] * self.N
        que = [s]
        level[s] = 0

        for v in que:
            for e_idx in self.near_edge[v]:
                w, cap = self.edge[e_idx]
                if cap and level[w] < 0:
                    level[w] = level[v] + 1
                    que.append(w)
        return (level[t] >= 0)

    def add_flow(self, s, t):
        goal = 0
        edge = self.edge
        stack = [(s, -1)]
        while stack:
            v, bfo_idx = stack[-1]

            if v == t:
                goal = 1

            if goal:
                if v == s:
                    return 1
                edge[bfo_idx][1] = 0
                edge[bfo_idx ^ 1][1] = 1
                stack.pop()
                continue

            for e_idx in self.ne_iter[v]:
                w, cap = edge[e_idx]
                if cap and self.level[v] < self.level[w]:
                    stack.append((w, e_idx))
                    break
            else:
                stack.pop()
        return 0

    def flow(self, s, t):
        flow = 0
        while self.is_connect(s, t):
            self.ne_iter = list(map(iter, self.near_edge))
            while self.add_flow(s, t):
                flow += 1
        return flow


def main():
    dicB = {bi: N+i+1 for i, bi in enumerate(B)}
    maxflow = Dinic(2*N + 2)
    nxt = [(0, 0), (T, 0), (T, T), (0, T), (-T, T),
           (-T, 0), (-T, -T), (0, -T), (T, -T)]

    for i in range(N):
        ax, ay = A[i]
        maxflow.add__edge(0, i+1, 1)
        for dx, dy in nxt[1:]:
            bx, by = ax+dx, ay+dy
            if (bx, by) in dicB:
                maxflow.add__edge(i+1, dicB[(bx, by)], 1)
    for i, (bx, by) in enumerate(B):
        maxflow.add__edge(N+i+1, 2*N+1, 1)

    cnt = maxflow.flow(0, 2*N+1)
    if cnt < N:
        return print("No")

    print("Yes")
    ans = []
    for i in range(N):
        ax, ay = A[i]
        for e_idx in maxflow.near_edge[i+1]:
            v, f = maxflow.edge[e_idx]
            if v > N and f == 0:
                bx, by = B[v-1-N]
                ans.append(nxt.index((bx - ax, by - ay)))
                break
    return print(*ans)


"""if __name__ == '__main__':
    N, T = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    B = [tuple(map(int, input().split())) for _ in range(N)]

    main()"""

if __name__ == '__main__':
    N2 = 141
    N, T = N2**2, 1
    A = [(i, j) for i in range(N2) for j in range(N2)]
    B = [(i, j) for i in range(N2) for j in range(N2)]

    main()
