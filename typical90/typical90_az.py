def main():
    ans = 1
    for ai in A:
        ans = ans * sum(ai) % MOD1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    MOD1 = 10**9 + 7

    main()
