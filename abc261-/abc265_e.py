from collections import Counter


def main():
    dp = {(0, 0): 1}
    for _ in range(N):
        nxt = Counter()
        for (x, y), c in dp.items():
            c %= MOD9
            if (x+A, y+B) not in XY:
                nxt[(x+A, y+B)] += c
            if (x+C, y+D) not in XY:
                nxt[(x+C, y+D)] += c
            if (x+E, y+F) not in XY:
                nxt[(x+E, y+F)] += c
        dp = nxt
    return print(sum(dp.values()) % MOD9)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A, B, C, D, E, F = map(int, input().split())
    XY = set(tuple(map(int, input().split())) for _ in range(M))
    MOD9 = 998244353

    main()
