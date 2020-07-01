from itertools import permutations


def nearlist(N, LIST):  # 隣点リスト
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ans, near = 0, nearlist(n, ab)
for l in permutations(range(1, n), n - 1):
    s = 0
    for i in l:
        t = i
        if t not in near[s]:
            break
        s = t
    else:
        ans += 1
print(ans)
