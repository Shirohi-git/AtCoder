def main():
    ans = 1
    for i, ci in enumerate(C):
        ans = ans * max(ci-i, 0) % MOD1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    C = sorted(map(int, input().split()))
    MOD1 = 10**9 + 7

    main()
