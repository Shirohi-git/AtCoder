def back_dfs(s0, n0, near0):
    flag = [0] * n0
    flag[s0] = 1
    stack = [s0]
    near_it = [iter(ni) for ni in near0]

    while stack:
        q = stack[-1]
        for i in near_it[q]:
            if len(stack) > 1 and i == stack[-2]:
                continue
            if flag[i]:
                idx = stack.index(i)
                return stack[idx:]
            flag[i] = 1
            stack.append(i)
            break
        else:
            stack.pop()
    return


class Unionfind():
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


def main():
    def nearlist(n0, LIST):
        res = [[] for _ in range(n0)]
        for a, b in LIST:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, UV)
    stk = back_dfs(0, N, near) * 2
    loop = {*map(tuple, zip(stk, stk[1:]))}

    uf = Unionfind(N)
    for u, v in UV:
        u, v = u-1, v-1
        if (u, v) in loop or (v, u) in loop:
            continue
        uf.unite(u, v)

    for x, y in XY:
        print('Yes' if uf.same(x-1, y-1) else 'No')
    return


if __name__ == '__main__':
    N = int(input())
    UV = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    XY = [list(map(int, input().split())) for _ in range(Q)]

    main()
