def main():
    res = 0
    mx, mn = max(A), min(A)

    if mx == mn:
        res |= (mx == N-1 or 2*mx <= N)
    if mx == mn+1:
        c = A.count(mn)
        res |= (2*mx-N <= c <= mn)
    return print("Yes" if res else "No")


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
