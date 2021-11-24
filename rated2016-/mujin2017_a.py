def main():

    def factorial(num):
        res = 1
        for i in range(1, num+1):
            res = res * i % MOD1
        return res

    ans, cnt, bfo = 1, 0, 0
    for xi in X:
        if bfo < 2*cnt - 1:
            ans = ans * cnt % MOD1
            cnt -= 1
        cnt, bfo = cnt+1, xi
    ans *= factorial(cnt)
    return print(ans % MOD1)


if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    MOD1 = 10**9 + 7

    main()
