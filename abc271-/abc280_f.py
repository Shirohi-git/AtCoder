class Unionfind:
    def __init__(self, n0):
        self.n = n0
        self.len = n0
        self.parents = [-1] * n0

    def find(self, x):
        stack = []
        while self.parents[x] >= 0:
            stack.append(x)
            x = self.parents[x]
        for i in stack:
            self.parents[i] = x
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.len -= 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_members(self):
        group = {i: [] for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.n):
            group[self.find(i)].append(i)
        return group


def main():
    def weighted_nearlist(n0, lst0):
        res = [set() for _ in range(n0)]
        for a, b, w in lst0:
            uf.unite(a-1, b-1)
            res[a-1].add((b-1, w))
            res[b-1].add((a-1, -w))
        return res

    def all_inf(r):
        for vi in mem[r]:
            dist[vi] = 'inf'

    def bfs(s0):
        dist[s0] = 0
        que = [s0]
        for q in que:
            for i, w in near[q]:
                if dist[i] == None:
                    dist[i] = w + dist[q]
                    que.append(i)
                elif dist[i] != w + dist[q]:
                    return all_inf(s0)
        return

    uf = Unionfind(N)
    near = weighted_nearlist(N, ABC)
    mem = uf.all_members()
    dist = [None] * N
    for v in uf.roots():
        bfs(v)

    ans = []
    for x, y in XY:
        if not uf.same(x-1, y-1):
            ans.append('nan')
        elif dist[x-1] == 'inf':
            ans.append('inf')
        else:
            ans.append(dist[y-1] - dist[x-1])
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    XY = [list(map(int, input().split())) for _ in range(Q)]

    main()
