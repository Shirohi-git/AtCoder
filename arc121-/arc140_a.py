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
    div = makedivisor(N)
    ans = N
    for di in div:
        cnt = [Counter(S[i::di]) for i in range(di)]
        res = sum(max(ci.values()) for ci in cnt)
        if N - res <= K:
            ans = min(ans, di)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()

    main()
