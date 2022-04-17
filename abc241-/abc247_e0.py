def main():
    sublst = []
    l = 0
    for r in range(N+1):
        if not Y <= A[r] <= X:
            a_lr = A[l:r]
            if a_lr and max(a_lr) == X and min(a_lr) == Y:
                sublst.append(a_lr)
            l = r + 1

    ans = 0
    for sl in sublst:
        mx, mn = -1, -1
        for i, v in enumerate(sl):
            if v == X:
                mx = i
            if v == Y:
                mn = i
            if min(mx, mn) > -1:
                ans += min(mx, mn) + 1
    return print(ans)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split())) + [X+1]

    main()
