def main():
    dp = [10**10] * N
    st = T.index(min(T))
    for i in range(st, st+N):
        now, bfo = i % N, (i-1) % N
        dp[now] = min(T[now], dp[bfo]+S[bfo])
    return print(*dp, sep='\n')


if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    main()
