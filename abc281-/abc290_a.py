def main():
    ans = 0
    for bi in B:
        ans += A[bi-1]
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
