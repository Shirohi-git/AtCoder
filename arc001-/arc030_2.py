import sys
sys.setrecursionlimit(10 ** 7)

class Recursive_dfs():  # 深優先探索(再帰)  # スタック
    # 隣点リスト,始点,数
    def __init__(self, NEAR, S, N, H):
        self.frag = set([S])
        self.h, self.near = H, NEAR
        self.cnt = 0

    def recdfs(self, p):
        for i in self.near[p]:  # 移動先の候補
            if i in self.frag:  # 処理済みか否か
                continue
            self.frag.add(i)
            self.recdfs(i)
            if self.h[i] == 1:
                self.cnt += 2
                self.h[p] = 1
        return self.cnt

n, x = map(int, input().split())
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]

near = [[] for _ in range(n)]
for a, b in ab:
    near[a - 1].append(b - 1)
    near[b - 1].append(a - 1)

ans = Recursive_dfs(near, x - 1, n, h)
print(ans.recdfs(x-1))
