def main():
    def accsum(x):
        return x*(x+1)//2

    ans, num = 0, 1
    while num <= N:
        ans += accsum(min(N+1, num*10) - num)
        num *= 10
    return print(ans % MOD9)


if __name__ == '__main__':
    N = int(input())
    MOD9 = 998244353

    main()