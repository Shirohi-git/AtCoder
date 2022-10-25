def main():
    def dp(ini, a):
        st = {ini}
        for ai in a:
            nxt = set()
            for si in st:
                nxt.add(si+ai), nxt.add(si-ai)
            st = nxt
        return st

    col, row = dp(0, A[1::2]), dp(A[0], A[2::2])
    res = (X in row and Y in col)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    main()
