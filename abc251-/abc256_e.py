class Strongly_Conected_Component():

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

        self.grp = [[] for _ in range(self.cnt)]
        for i in range(self.n):
            self.grp[self.idx[i]].append(i)
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
    scc = Strongly_Conected_Component(N, [[xi-1] for xi in X])
    ans = sum(min(C[v] for v in gi) for gi in scc.grp if len(gi) > 1)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    C = list(map(int, input().split()))

    main()
