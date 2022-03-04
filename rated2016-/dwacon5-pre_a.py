def main():
    ave, ans, dif = sum(A), 0, max(A) * N
    for i in range(N):
        if abs(ave - A[i] * N) < dif:
            ans, dif = i, abs(ave - A[i] * N)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
