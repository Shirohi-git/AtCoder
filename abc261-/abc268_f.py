def main():
    def evaluate(s):
        cnt, xc = 0, 0
        for si in s:
            if si == 'X':
                xc += 1
            else:
                cnt += int(si)
        return -xc * INF // cnt

    x, num, el = [], [], []
    xcnt = 0
    for si in S:
        if 'X' not in si:
            num.append(si)
        elif 'X' * len(si) == si:
            x.append(si)
        else:
            el.append(si)
        xcnt += si.count('X')

    el = sorted(el, key=lambda x: evaluate(x))
    res = ''.join(x + el + num)

    ans, xcnt = 0, 0
    for ri in res:
        if ri == 'X':
            xcnt += 1
        else:
            ans += int(ri) * xcnt
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    INF = 10**10

    main()
