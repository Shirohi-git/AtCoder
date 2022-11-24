def main():
    ans = A[K:] + [0]*K
    return print(*ans[:N])


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
