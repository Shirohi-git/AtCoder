from heapq import heappop, heappush


class Unionfind():
    def __init__(self, n0):
        self.n = n0
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def all_members(self):
        group = {i: set() for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.n):
            group[self.find(i)].add(i)
        return group


def solve(edg):
    def div_one_two(itr):
        for i in itr:
            if len(edg[i]) == 1:
                one.append(i)
            elif len(edg[i]) > 1:
                heappush(two, (len(edg[i]), i))
        return

    res = []
    one, two = [], []
    div_one_two(range(len(edg)))

    while one or two:
        if (not one) or ((not two) and (len(one) != 2)):
            return [[-1]]
        if (not two) and (len(one) == 2):
            s, t = one.pop(), one.pop()
            res.append((edg[s].pop(), edg[t].pop()))

        nxt = []
        while one:
            if not two:
                break
            s, (_, t) = one.pop(), heappop(two)
            nxt.append(t)
            res.append((edg[s].pop(), edg[t].pop()))
        div_one_two(nxt)
    return res


def main():
    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in AB:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N)
    is_small = any(D[i] < len(near[i]) for i in range(N))
    if sum(D)//2 != N-1 or is_small:
        return print(-1)

    uf = Unionfind(N)
    for a, b in AB:
        if uf.same(a-1, b-1):
            return print(-1)
        uf.unite(a-1, b-1)
    mem = uf.all_members()

    edge = []
    for k in mem:
        tmp = []
        for v in mem[k]:
            tmp += [v+1] * (D[v] - len(near[v]))
        if tmp:
            edge.append(tmp)

    for ai in solve(edge):
        print(*ai)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    D = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
