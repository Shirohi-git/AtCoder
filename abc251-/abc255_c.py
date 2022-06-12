def main():
    mn, mx = A, A + D*(N-1)
    ans = min(abs(X - mn), abs(X - mx))
    if mx < mn:
        mn, mx = mx, mn
    d = abs(D)
    if mn <= X <= mx and d != 0:
        ans = min((A % d - X % d) % d, (X % d - A % d) % d)
    return print(ans)


if __name__ == '__main__':
    X, A, D, N = map(int, input().split())

    main()
