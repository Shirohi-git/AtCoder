def main():
    ans, now = 0, N-1
    while now:
        ans += 1
        now = P[now-1]-1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    main()
