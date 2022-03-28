def main():
    ans = [0] * (M+1)
    c = C[:]
    for i in range(N+1):
        if A[i] != 0:
            idx, top = i, A[i]
            break

    for i in range(M+1):
        ans[i] = c[i+idx] // top
        for j in range(N+1):
            c[i+j] -= ans[i] * A[j]
    return print(*ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    main()
