class func_near():
    def nearloop(self, r1, r2, rev):
        res = [-1] * (H*W)
        for j in range(r1):
            bfo = 1
            for i in range(r2):
                x, y = (i, j) if rev else (j, i)
                if GRID[x][y] == '.':
                    self.cnt += bfo
                    res[x*W + y] = self.cnt
                bfo = (GRID[x][y] == '#')
        return res

    def __init__(self):
        self.cnt = -1
        self.col = self.nearloop(W, H, 1)
        self.row = self.nearloop(H, W, 0)
        self.idx = [(self.col[i], self.row[i]) for i in range(H*W)]

        maxidx = max(self.row) + 1
        self.flag = [0] * maxidx
        self.dic = [[] for _ in range(maxidx)]
        for i in range(H*W):
            if self.col[i] == -1:
                continue
            self.dic[self.col[i]].append(i)
            self.dic[self.row[i]].append(i)


def bfs(S, G):
    dist = [-2] * (H*W)
    dist[S] = -1

    que = [S]
    for q in que:
        lst = []
        for i in NEAR.idx[q]:
            if NEAR.flag[i] == 0:
                lst += NEAR.dic[i]
                NEAR.flag[i] = 1
        for i in lst:
            if dist[i] == -2:
                dist[i] = dist[q] + 1
                que.append(i)
        if dist[G] > -2:
            return dist[G]


if __name__ == '__main__':
    H, W = map(int, input().split())
    SX, SY = map(lambda x: int(x)-1, input().split())
    TX, TY = map(lambda x: int(x)-1, input().split())
    GRID = [input() for _ in range(H)]

    NEAR = func_near()
    ANS = bfs(SX*W + SY, TX*W + TY)
    print(ANS)
