def main():
    bfo, ans = 0, 10**20
    for i, (ai, bi) in enumerate(AB[:X], 1):
        bfo += ai + bi
        ans = min(ans, bfo + bi*(X-i))
    return print(ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
