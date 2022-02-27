from collections import Counter


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

    def add__edge_win(self, res, v1, v2, v12):
        if res != -1:
            self.add__edge(v12, v1, 1)
        if res != 1:
            self.add__edge(v12, v2, 1)
        return

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
        stack = [(s, self.INF, -1)]
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
            f = self.INF
            while f:
                f = self.add_flow(s, t)
                flow += f
        return flow


def main():

    def v_idx(v):
        if v in ['s', 't']:
            return [0, v_cnt-1][v == 't']
        elif type(v) == int:
            return v_cnt - (N+1) + v
        else:
            x, y = v
            if x < y:
                x, y = y, x
            return 1 + x*(x-1)//2 + y

    v_cnt = 1 + N*(N-1)//2 + N + 1
    s, t = v_idx('s'), v_idx('t')
    lose = Counter(l-1 for _, l in WL)

    ans = []
    for p in range(N):
        win = MAX_WIN - lose[p] - 1
        dnc = Dinic(v_cnt)
        for i in range(N):
            vi = v_idx(i)
            dnc.add__edge(vi, t, win+(i == p))
            for j in range(i):
                vj, vij = v_idx(j), v_idx((i, j))
                res = ((i+1, j+1) in WL) - ((j+1, i+1) in WL)
                dnc.add__edge(s, vij, 1)
                dnc.add__edge_win(res, vi, vj, vij)

        mx_f = dnc.flow(s, t)
        if mx_f == N*(N-1)//2:
            ans.append(p+1)
    return print(*ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    WL = set(tuple(map(int, input().split())) for _ in range(M))
    MAX_WIN = N-1

    main()
