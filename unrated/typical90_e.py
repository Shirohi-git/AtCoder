def loop(b, p, lst1, lst2):
    res = [0] * b
    for i in range(b):
        for j in range(b):
            nxt = (i * p + j) % b
            res[nxt] += lst1[i] * lst2[j]
            res[nxt] %= MOD1
    return res


def main():
    n, b, k = map(int, input().split())
    c = list(map(int, input().split()))

    pow10 = [10 % b]
    for i in range(60):
        pow10 += [pow10[i]**2 % b]

    dp = [[0] * b for _ in range(61)]
    for ci in c:
        dp[0][ci % b] += 1
    for p in range(60):
        dp[p+1] = loop(b, pow10[p], dp[p], dp[p])

    ans = [0] * b
    ans[0] = 1
    for p in range(60):
        if (n >> p) & 1:
            ans = loop(b, pow10[p], ans, dp[p])
    print(ans[0])


if __name__ == '__main__':
    MOD1 = 10**9 + 7
    main()
