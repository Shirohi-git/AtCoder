def main():
    from itertools import permutations

    res = 0
    for l in permutations(range(1, N+1)):
        new = set(tuple(sorted([l[ci-1], l[di-1]])) for ci, di in CD)
        res |= (new == AB)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = set(tuple(sorted(map(int, input().split()))) for _ in range(M))
    CD = [list(map(int, input().split())) for _ in range(M)]

    main()
