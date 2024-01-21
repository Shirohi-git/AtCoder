def lcp(a, b):
    for i, si, ti in zip(range(len(a)), a, b):
        if si != ti:
            return i
    return min(len(a), len(b))


def main():
    ans = {si: 0 for si in S}

    s = [''] + sorted(S) + ['']
    bfo = lcp('', s[1])
    for x, y in zip(s[1:], s[2:]):
        now = lcp(x, y)
        ans[x] = max(now, bfo)
        bfo = now

    return print(*[ans[si] for si in S], sep='\n')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()
