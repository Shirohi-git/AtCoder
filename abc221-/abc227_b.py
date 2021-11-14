def main():
    res = set()
    for a in range(1, 150):
        for b in range(1, 150):
            res.add(4*a*b + 3*(a+b))

    ans = 0
    for si in S:
        ans += (si not in res)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))

    main()
