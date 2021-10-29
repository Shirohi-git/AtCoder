def main():
    from collections import Counter

    def make_nxt(lst):
        res = []
        for idx in lst: 
            tpl = tuple(sorted([idx, a_rev[idx].pop()]))
            if cnt[tpl] == 1:
                res += list(tpl)
            cnt[tpl] ^= 1
        return res

    a_rev = [[-1] + ai[::-1] for ai in A]
    cnt = Counter()

    day = 0
    nxt = make_nxt(range(N))
    while any(ri for ri in a_rev):
        day += 1
        now = nxt[::]
        if not now:
            return print(-1)
        nxt = make_nxt(now)
    return print(day)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]

    main()
