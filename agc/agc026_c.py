def main():
    from collections import Counter
    from itertools import product

    def paint(t, b, c):
        return ''.join(t[i] for i in range(N) if b[i] == c)

    sl, sr = S[:N], S[N:]
    cnt = Counter()
    for bit in product([0, 1], repeat=N):
        lred, lblue = paint(sl, bit, 0), paint(sl, bit, 1)
        cnt[(lred, lblue[::-1])] += 1

    ans = 0
    for bit in product([0, 1], repeat=N):
        rred, rblue = paint(sr, bit, 0), paint(sr, bit, 1)
        ans += cnt[(rblue[::-1], rred)]
    return print(ans)


if "__main__":
    N, S = int(input()), input()

    main()
