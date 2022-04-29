def main():
    ans = [0] * N
    for i in range(1, N):
        if A[i-1] > A[i]:
            ans[i-1] ^= 1
            ans[i] ^= 1
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
