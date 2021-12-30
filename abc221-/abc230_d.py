def main():
    lr = sorted(LR, key=lambda x: (x[1], x[0]))
    ans, dl = 0, -2*D
    for l, r in lr:
        if dl + D - 1 < l:
            ans += 1
            dl = r
    return print(ans)


if __name__ == '__main__':
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]

    main()
