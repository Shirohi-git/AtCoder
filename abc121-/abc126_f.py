def main():
    if K >= pow(2, M) or M == K == 1:
        return print(-1)
    if M == K+1 == 1:
        return print(*[0, 0, 1, 1])
    lst = [i for i in range(pow(2, M)) if i != K]
    ans = lst + [K] + lst[::-1] + [K]
    return print(*ans)


if __name__ == '__main__':
    M, K = map(int, input().split())

    main()
