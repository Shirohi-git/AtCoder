def main():
    dp = {0}
    for ti in T:
        nxt = set(dp)
        for di in dp:
            nxt.add(di + ti)
        dp = set(nxt)

    ans = sum(T)
    sum_t = diff = sum(T)
    for di in dp:
        if abs(sum_t//2 - di) < diff:
            ans, diff = di, abs(sum_t//2 - di)
    return print(max(ans, sum_t-ans))


if __name__ == '__main__':
    N = int(input())
    T = list(map(int, input().split()))

    main()
