def main():
    def solve(num):
        res = 0
        for i in range(1, 20):
            if num < pow(10, i-1):
                break
            min_n = pow(10, i-1, MOD1)
            max_n = min(pow(10, i) - 1, num) % MOD1
            cnt = (max_n*(max_n+1) - (min_n-1)*min_n)//2 % MOD1
            res += i * cnt % MOD1
        return res

    ans = (solve(R) - solve(L-1)) % MOD1
    return print(ans)


if __name__ == '__main__':
    L, R = map(int, input().split())
    MOD1 = 10**9 + 7

    main()
