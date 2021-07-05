def main():
    ans = 0
    for i, (li, ri) in enumerate(LR):
        for lj, rj in LR[:i]:
            cnt, div = 0, (ri-li+1) * (rj-lj+1)
            for p in range(li, ri+1):
                for q in range(lj, rj+1):
                    cnt += (q > p)
            ans += cnt / div
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    main()
