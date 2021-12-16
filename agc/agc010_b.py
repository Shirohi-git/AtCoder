def main():
    cnt, res = divmod(2 * sum(A), N * (N+1))
    s_cnt = [0] * N
    for i in range(N):
        s_cnt[i], mod = divmod(A[i-1] - A[i] + cnt, N)
        res |= mod | (s_cnt[i] < 0)
    res |= (sum(s_cnt) != cnt)
    print("YES" if res == 0 else "NO")


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
