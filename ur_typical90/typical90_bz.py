def nearlist(n0, lst0):
    res = [0 for _ in range(n0)]
    for a, b in lst0:
        res[max(a, b) - 1] += 1
    return res


def main():
    near = nearlist(N, AB)
    ans = sum(ni == 1 for ni in near)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
