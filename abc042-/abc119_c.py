from itertools import product


def solve(T, PTTN):
    lst = [l[i] for i, t in enumerate(PTTN) if t == T]
    if lst:
        ANS = (len(lst) - 1) * 10
        ANS += abs(sum(lst) - tgt[T])
        return ANS
    return 10 ** 5


tgt = list(map(int, input().split()))
l = [int(input()) for _ in range(tgt[0])]

ans = 10 ** 5
for pttn in product([0, 1, 2, 3], repeat=tgt[0]):
    tmp = sum(solve(i + 1, pttn) for i in range(3))
    ans = min(ans, tmp)
print(ans)
