def main():
    for k in K:
        d, m, dm, ans = 0, 0, 0, 0
        for i in range(N):
            if i >= k:
                sik = S[i-k]
                d, dm = d - (sik == D), dm - m * (sik == D)
                m -= (sik == M)
            si = S[i]
            d += (si == D)
            m, dm = m + (si == M), dm + d * (si == M)
            ans += dm * (si == C)
        print(ans)
    return


if __name__ == '__main__':
    N, S = int(input()), input()
    Q = int(input())
    K = list(map(int, input().split()))
    D, M, C = 'DMC'

    main()
