def main():
    dp_a, dp_b = [0] * N, [0] * N
    dp_a[0] = dp_b[0] = 1

    for i in range(1, N):
        if dp_a[i-1]:
            dp_a[i] |= (abs(A[i-1] - A[i]) <= K)
            dp_b[i] |= (abs(A[i-1] - B[i]) <= K)
        if dp_b[i-1]:
            dp_a[i] |= (abs(B[i-1] - A[i]) <= K)
            dp_b[i] |= (abs(B[i-1] - B[i]) <= K)
    res = (dp_a[-1] | dp_b[-1])
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
