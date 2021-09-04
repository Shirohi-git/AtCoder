def main():
    ans = 1
    for i in range(N):
        ans = ans * (i+1) % MOD1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    MOD1 = 10**9 + 7
    main()
