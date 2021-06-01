from collections import Counter


def nearlist(n0):
    NEAR = [[] for _ in range(n0)]
    for a, b in AB:
        NEAR[a - 1].append(b - 1)
    return NEAR


class strongly_conected_component():

    def __init__(self, n0, near0):
        self.n = n0
        self.near = [ni[:] for ni in near0]
        self.nm_near = [iter(ni) for ni in near0]
        self.rv_near = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in near0[i]:
                self.rv_near[j].append(i)

        self.flag_dfs = [0] * self.n
        self.order = []
        for i in range(self.n):
            if not self.flag_dfs[i]:
                self.dfs(i)

        self.cnt = 0
        self.flag_rdfs = [0] * self.n
        self.idx = [-1] * self.n
        for i in self.order[::-1]:
            if not self.flag_rdfs[i]:
                self.rdfs(i)
                self.cnt += 1
        return

    def dfs(self, v):
        self.flag_dfs[v] = 1
        stack = [v]

        while stack:
            now = stack[-1]
            for nxt in self.nm_near[now]:
                if not self.flag_dfs[nxt]:
                    self.flag_dfs[nxt] = 1
                    stack.append(nxt)
                    break
            else:
                stack.pop()
                self.order.append(now)
        return

    def rdfs(self, v):
        self.idx[v] = self.cnt
        stack = [v]

        while stack:
            now = stack.pop()
            if self.flag_rdfs[now]:
                continue
            self.flag_rdfs[now] = 1
            for nxt in self.rv_near[now]:
                if not self.flag_rdfs[nxt]:
                    self.idx[nxt] = self.cnt
                    stack.append(nxt)
        return


def main():
    near = nearlist(N)
    scc = strongly_conected_component(N, near)
    ans = sum(ci * (ci-1) for ci in Counter(scc.idx).values())
    return print(ans // 2)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = set(tuple(map(int, input().split())) for _ in range(M))

    main()
