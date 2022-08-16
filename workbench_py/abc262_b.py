def main():
    uv = set((min(u, v), max(u, v)) for u, v in UV)
    ans = 0
    for i in range(1, N+1):
        for j in range(1, i):
            for k in range(1, j):
                edge = [(k, j), (k, i), (j, i)]
                ans += all(ei in uv for ei in edge)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [tuple(map(int, input().split())) for _ in range(M)]

    main()
