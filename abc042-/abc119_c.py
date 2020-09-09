from itertools import product


def solve(NUM, LIST):
    lst = [l[i] for i, t in enumerate(LIST) if t == NUM]
    if len(lst) == 0:
        return 10 ** 5
    ANS = (len(lst) - 1) * 10
    ANS += abs(sum(lst) - tgt[NUM])
    return ANS


tgt = list(map(int, input().split()))
l = [int(input()) for _ in range(tgt[0])]

ans = 10 ** 5
for pttn in product([0, 1, 2, 3], repeat=tgt[0]):
    tmp = sum(solve(i + 1, pttn) for i in range(3))
    ans = min(ans, tmp)
print(ans)
