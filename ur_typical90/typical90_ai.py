def nearlist(n0):
    res = [[] for _ in range(n0)]
    for a, b in AB:
        res[a - 1].append(b - 1)
        res[b - 1].append(a - 1)
    return res


def dfs(s0, n0):
    idx, dist = [-1] * n0, [-1] * n0
    flag = [-1] * n0
    dist[s0], flag[s0] = 0, 0
    stack = [s0]

    id = 0
    while stack:
        q = stack[-1]
        for i in NEAR[q]:
            if flag[i] > -1:
                continue
            flag[i] = flag[q] + 1
            stack.append(i)
            break
        else:
            q = stack.pop()
            idx[q], dist[id] = id, flag[q]
            id += 1
    return idx, dist


class SparseTable():

    def stfunc(self, x, y):
        return min(x, y)

    def __init__(self, lst0):
        n = len(lst0)
        num = n.bit_length()
        table = [lst0] + [[-1] * n for _ in range(num - 1)]
        bfo = table[0]
        for i in range(1, num):
            pow2 = (1 << (i - 1))
            for j in range(n - (1 << i) + 1):
                table[i][j] = self.stfunc(bfo[j], bfo[j + pow2])
            bfo = table[i][:]
        self.table = table

    def query(self, l, r):
        i = (r - l).bit_length() - 1
        return self.stfunc(self.table[i][l], self.table[i][r - (1 << i)])


def main():
    for i in range(Q):
        que = sorted(Idx[vij-1] for vij in V[i])[::-1]
        p = que[-1]

        edge = 0
        while len(que) > 1:
            q = que.pop()
            d_lca = ST.query(q, que[-1]) - 1
            edge += Dist[q] + Dist[que[-1]] - 2 * d_lca
        d_pq = ST.query(p, que[-1]) - 1
        edge += Dist[p] + Dist[que[-1]] - 2 * d_pq
        print(edge // 2)
    return


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    Q = int(input())
    V = [list(map(int, input().split()))[1:] for _ in range(Q)]

    NEAR = [iter(ni) for ni in nearlist(N)]
    Idx, Dist = dfs(0, N)
    ST = SparseTable(Dist)
    main()
