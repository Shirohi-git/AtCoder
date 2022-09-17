def main():
    dt = sorted(tdi[::-1] for tdi in TD)[::-1]
    top = 0
    mid, flag = [], set()
    for di, ti in dt[:K]:
        if ti not in flag:
            flag.add(ti)
            top += di
        else:
            mid += [di]

    cnt = len(flag)
    change = []
    for di, ti in dt[K:]:
        if ti not in flag:
            flag.add(ti)
            change += [di]

    bfo = ans = top + sum(mid) + cnt**2
    for mi, ci in zip(mid[::-1], change):
        res = bfo + ci-mi + 2*cnt+1
        cnt += 1
        bfo, ans = res, max(ans, res)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    TD = [list(map(int, input().split())) for _ in range(N)]

    main()
