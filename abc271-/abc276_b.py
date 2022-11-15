def main():
    def nearlist(n0, lst):
        res = [[] for _ in range(n0)]
        for a, b in lst:
            res[a - 1].append(b)
            res[b - 1].append(a)
        return res

    near = nearlist(N, AB)
    for ni in near:
        ans = [len(ni)] + sorted(ni)
        print(*ans)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
