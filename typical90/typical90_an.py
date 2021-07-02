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
        stack = [(s, INF, -1)]
        while stack:
            v, bfo_cap, bfo_idx = stack[-1]

            if v == t:
                goal, res = 1, bfo_cap

            if goal:
                if v == s:
                    return res
                edge[bfo_idx][1] -= res
                edge[bfo_idx ^ 1][1] += res
                stack.pop()
                continue

            for e_idx in self.ne_iter[v]:
                w, cap = edge[e_idx]
                if cap and self.level[v] < self.level[w]:
                    stack.append((w, min(bfo_cap, cap), e_idx))
                    break
            else:
                stack.pop()
        return 0

    def flow(self, s, t):
        flow = 0
        while self.is_connect(s, t):
            self.ne_iter = list(map(iter, self.near_edge))
            f = INF
            while f:
                f = self.add_flow(s, t)
                flow += f
        return flow


def main():
    maxflow = Dinic(N+2)
    for i in range(N):
        maxflow.add__edge(0, i+1, A[i])
        maxflow.add__edge(i+1, N+1, W)
        for cij in C[i]:
            maxflow.add__edge(cij, i+1, INF)
    ans = sum(A) - maxflow.flow(0, N+1)
    return print(ans)


if __name__ == '__main__':
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    C = [list(map(int, input().split()))[1:] for _ in range(N)]
    INF = 10**10

    main()
