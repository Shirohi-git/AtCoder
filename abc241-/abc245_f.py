from collections import Counter


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

    def construct(self):
        graph = [set() for _ in range(self.cnt)]
        for v in range(self.n):
            v_id = self.idx[v]
            for w in self.near[v]:
                w_id = self.idx[w]
                if v_id != w_id:
                    graph[v_id].add(w_id)
        return graph


def back_dfs(n0, near0, cnt0):
    is_loop = [0] * n0
    flag = [0] * n0
    near_it = [iter(ni) for ni in near0]

    res = 0
    for i in range(n0):
        if flag[i]:
            continue
        stack = [i]
        while stack:
            q = stack[-1]
            for i in near_it[q]:
                if flag[i]:
                    continue
                flag[i] = 1
                stack.append(i)
                break
            else:
                is_loop[q] |= (cnt0[q] > 1)
                is_loop[q] |= any(is_loop[i] for i in near0[q])
                if is_loop[q] == 0:
                    res += cnt0[q]
                stack.pop()
    return res


def main():
    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
        return res

    near = nearlist(N, UV)
    scc = Strongly_Conected_Component(N, near)
    scc_v, scc_near = Counter(scc.idx), scc.construct()
    ans = back_dfs(len(scc_v), scc_near, scc_v)
    return print(N - ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]

    main()
