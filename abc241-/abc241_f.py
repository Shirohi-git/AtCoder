from bisect import bisect
from collections import defaultdict


class Block:
    def __init__(self, is_col):
        self.is_col = is_col
        self.block = defaultdict(list)

    def add(self, x, y):
        if self.is_col:
            x, y = y, x
        self.block[x-1].append(y-1)
        return

    def stop(self, x, y):
        if self.is_col:
            x, y = y, x
        res = []
        if not self.block[x]:
            return res
        id = bisect(self.block[x], y)
        if id != 0:
            res += [(x, self.block[x][id-1]+1)]
        if id < len(self.block[x]):
            res += [(x, self.block[x][id]-1)]
        if self.is_col:
            res = [ri[::-1] for ri in res]
        return res


def main():
    def search_stop(x, y):
        res = H_block.stop(x, y)
        res += W_block.stop(x, y)
        return res

    def grid_bfs(s0, h0, w0):
        sx, sy = s0
        flag = {(sx, sy): 0}
        que = [s0]

        for qx, qy in que:
            qd = flag[(qx, qy)]
            for px, py in search_stop(qx, qy):
                if 0 <= px < h0 and 0 <= py < w0:
                    if (px, py) in flag:
                        continue
                    flag[(px, py)] = qd + 1
                    que.append((px, py))
        return flag

    H_block, W_block = Block(False), Block(True)
    for x, y in sorted(XY):
        H_block.add(x, y), W_block.add(x, y)

    s, g = (SX-1, SY-1), (GX-1, GY-1)
    dist = grid_bfs(s, H, W)
    ans = dist[g] if (g in dist) else -1
    return print(ans)


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    SX, SY = map(int, input().split())
    GX, GY = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
