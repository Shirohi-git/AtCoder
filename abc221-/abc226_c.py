def main():
    ans = 0
    now, need = set([N]), set([N])
    while now:
        nxt = set()
        for i in now:
            t, _, *a = TKA[i-1]
            ans += t
            for ai in a:
                if ai not in need:
                    nxt.add(ai), need.add(ai)
        now = set(nxt)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    TKA = [list(map(int, input().split())) for _ in range(N)]

    main()
