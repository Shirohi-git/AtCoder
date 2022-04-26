from collections import Counter


def makedivisor(n0):
    p, upper, lower = 1, [], []
    while p * p <= n0:
        if n0 % p == 0:
            lower.append(p)
            if p * p != n0:
                upper.append(n0 // p)
        p += 1
    return lower + upper[::-1]


def main():
    ans = 0
    cnt = Counter(A)
    for ai in A:
        for aj in makedivisor(ai):
            if cnt[aj]:
                ans += cnt[ai // aj] * cnt[aj]
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
