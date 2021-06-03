def main():
    cnt = K
    for i in range(N):
        cnt -= abs(A[i] - B[i])
    res = (cnt < 0 or cnt % 2)
    return print("No" if res else "Yes")


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
