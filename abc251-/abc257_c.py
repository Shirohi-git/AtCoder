from itertools import accumulate


def main():
    s_wei = sorted(W)
    s_idx = sorted(range(N), key=lambda x: W[x])
    acc = [*accumulate([0]+[int(S[wi]) for wi in s_idx])]

    ans = acc[N]
    for i in range(1, N+1):
        now = acc[N]-acc[i] + i-acc[i]
        if i == N or s_wei[i-1] != s_wei[i]:
            ans = max(ans, now)
    return print(ans)


if __name__ == '__main__':
    N, S = int(input()), input()
    W = list(map(int, input().split()))

    main()
