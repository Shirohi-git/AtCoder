def main():
    ans = 1
    for i in range(60):
        cnt = 0
        for num in range(1 << N):
            for *xyz, w in XYZW:
                xyz_or = any(num >> (N-j) & 1 for j in xyz)
                if ((w >> i) & 1) != xyz_or:
                    break
            else:
                cnt += 1
        ans = ans * cnt % MOD1
    return print(ans)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    XYZW = [list(map(int, input().split())) for _ in range(Q)]
    MOD1 = 10**9 + 7

    main()
