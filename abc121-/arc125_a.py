def main():
    if len(set(T)-set(S)):
        return print(-1)

    cnt = 0
    if (1-S[0]) in S:
        cnt = min(S.index(1-S[0]), S[::-1].index(1-S[0])+1)
    ans, now, flag = 0, S[0], 0
    for ti in T:
        ans += 1
        if now != ti:
            ans += (1 if flag else cnt)
            now, flag = now ^ 1, 1
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    main()
