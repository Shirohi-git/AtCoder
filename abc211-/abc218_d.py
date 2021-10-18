def main():
    from collections import defaultdict

    dic = defaultdict(set)
    for i, (xi, yi) in enumerate(XY):
        for xj, yj in XY[i+1:]:
            if yi == yj:
                dic[(xi, xj)].add(yi)

    ans = 0
    for di in dic.values():
        ans += len(di) * (len(di)-1)
    return print(ans//2)


if __name__ == '__main__':
    N = int(input())
    XY = sorted(list(map(int, input().split())) for _ in range(N))

    main()
