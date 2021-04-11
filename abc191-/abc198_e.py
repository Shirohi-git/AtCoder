import sys
sys.setrecursionlimit(10 ** 7)


def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in ab:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


class Recursive_dfs():
    def __init__(self, S, N, NEAR):
        self.flag = [0] * N
        self.flag[S] = 1
        self.near = NEAR
        self.res = [1]

    def recdfs(self, p):
        for i in self.near[p]:
            if self.flag[i]:
                continue
            if ccnt[c[i] - 1] == 0:
                self.res.append(i + 1)
            ccnt[c[i] - 1] += 1
            self.flag[i] = 1
            self.recdfs(i)
            ccnt[c[i] - 1] -= 1


n = int(input())
c = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]

ccnt = [0] * max(c)
ccnt[c[0] - 1] = 1
near = nearlist(n)
rdfs = Recursive_dfs(0, n, near)
rdfs.recdfs(0)
print(*sorted(rdfs.res), sep='\n')
