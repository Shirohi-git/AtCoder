def main():
    ans = sum(pi * qi for pi, qi in PQ)
    ans += K * (ans < S)
    return print(ans)


if __name__ == '__main__':
    N, S, K = map(int, input().split())
    PQ = [list(map(int, input().split())) for _ in range(N)]

    main()
