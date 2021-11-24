def quotient(xy):
    from math import gcd
    x, y = xy
    if x == y == 0:
        return (0, 0)
    if (y < 0) or (y == 0 and x < 0):
        x, y = -x, -y
    t = gcd(x, y)
    return (x//t, y//t)


def main():
    from collections import Counter

    cnt = Counter()
    for ai, bi in map(quotient, AB):
        cnt[(ai, bi)] += 1
        cnt[quotient((-bi, ai))] += 0
    pow2 = [1]
    for _ in range(N):
        pow2.append(pow2[-1] * 2 % MOD1)

    ans = 1
    for (ai, bi), ci in cnt.items():
        if ai <= 0:
            continue
        cj = cnt[quotient((-bi, ai))]
        ans *= pow2[ci] + pow2[cj] - 1
        ans %= MOD1
    ans += -1 + cnt[(0, 0)]
    print(ans % MOD1)


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    MOD1 = 10**9 + 7

    main()
