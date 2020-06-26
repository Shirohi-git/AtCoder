import sys
sys.setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7

def memodp(DPW, DPB, near, x, FLAG):
    if DPW[x] + DPB[x] > 2:
        return (DPB[x] + DPW[x]) % mod
    else:
        for i in near[x]:
            if i not in FLAG:
                FLAG.add(i)
                DPW[x] *= memodp(DPW, DPB, near, i, FLAG)
                DPB[x] *= DPW[i]
        DPW[x], DPB[x] = DPW[x] % mod, DPB[x] % mod
        return (DPW[x] + DPB[x]) % mod


n = int(input())
xy = [list(map(int, input().split())) for i in range(n - 1)]

near = [[] for _ in range(n)]
for x, y in xy:
    near[x - 1].append(y - 1)
    near[y - 1].append(x - 1)

dpw, dpb, flag = [1] * n, [1] * n, set([0])
print(memodp(dpw, dpb, near, 0, flag))
