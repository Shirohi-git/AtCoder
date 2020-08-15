from itertools import product


def makelist(BIT):
    LIST, tmp = [], s[0]
    for si, bi in zip(s[1:], BIT):
        if bi == 1:
            LIST.append(tmp)
            tmp = si[:]
        elif bi == 0:
            tmp = [t + sij for t, sij in zip(tmp, si)]
    else:
        LIST.append(tmp)
    return LIST


def solve(LIST):
    COST, cnt = 0, [li[0] for li in LIST]
    if any(num > k for num in cnt):
        return h * w
    for j in range(1, w):
        tmp = [t + li[j] for t, li in zip(cnt, LIST)]
        if any(num > k for num in tmp):
            COST += 1
            cnt = [li[j] for li in LIST]
        else:
            cnt = tmp[:]
    return COST


h, w, k = map(int, input().split())
s = [[int(sij) for sij in input()] for _ in range(h)]

ans = h * w
for bit in product([0, 1], repeat=(h - 1)):
    numlist = makelist(bit)
    ans = min(ans, solve(numlist) + sum(bit))
print(ans)
