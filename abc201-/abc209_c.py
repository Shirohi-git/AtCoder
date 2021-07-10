def main():
    ans, num = 1, 0
    for i, ci in enumerate(C):
        ans = ans * max(ci-num, 0) % MOD1
        num = min(max(num, ci), i+1)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    C = sorted(map(int, input().split()))
    MOD1 = 10**9 + 7

    main()
