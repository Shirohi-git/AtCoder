def main():
    t, l = M, 0
    wt, wl = 0, 0
    ans = 0
    for si in S:
        if si == 0:
            t, wt, l, wl = t+wt, 0, 0, 0
        elif si == 1 and t > 0:
            t, wt = t-1, wt+1
        else:  # elif (si == 1 and t == 0) or si == 2:
            l, wl = l-1, wl-1
        ans = max(max(0, -t) + max(0, -l), ans)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = list(map(int, input()))

    main()
