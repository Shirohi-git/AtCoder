def main():
    ans = sorted(range(1, N+1), key=lambda x: -AB[x-1][0]*INF // sum(AB[x-1]))
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    INF = 10**20

    main()
