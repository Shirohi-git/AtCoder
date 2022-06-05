def main():
    ma = max(A)
    can = set(i+1 for i in range(N) if A[i] == ma)
    res = can & B
    return print("Yes" if res else "No")


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = set(map(int, input().split()))

    main()