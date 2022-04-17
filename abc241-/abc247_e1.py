def main():
    ans = 0
    l, mx, mn = -1, -1, -1
    for i, ai in enumerate(A):
        if not Y <= ai <= X:
            l, mx, mn = i, -1, -1
        if ai == X:
            mx = i
        if ai == Y:
            mn = i
        if min(mx, mn) > -1:
            ans += min(mx, mn) - l
    return print(ans)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split())) + [X+1]

    main()
