def main():
    a = [(A[i], i) for i in range(N)]
    b = [(B[i], i+N) for i in range(M)]
    c = sorted(a+b)
    ans_a, ans_b = [-1] * N, [-1] * M
    for id, (_, i) in enumerate(c):
        if i < N:
            ans_a[i] = id+1
        else:
            ans_b[i-N] = id+1
    return print(*ans_a), print(*ans_b)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
