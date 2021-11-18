def main():

    def fib(num):
        a, b = 0, 1
        for _ in range(num + 1):
            a, b = b, (a+b) % MOD1
        return a

    bit = sum((ci == 'B') << i for i, ci in enumerate(C))
    ans = 1
    if bit in [2, 3, 5, 13]:
        ans = pow(2, max(N-3, 0), MOD1)
    elif bit in [1, 6, 7, 9]:
        ans = fib(N-2)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    C = [input() for _ in range(4)]
    MOD1 = 10**9 + 7

    main()
