def main():
    cnt = sum(S[i] != T[i] for i in range(N))
    if cnt % 2:
        return print(-1)

    s = t = cnt//2
    ans = ['_'] * N
    for i, si, ti in zip(range(N), S, T):
        if si == ti:
            ans[i] = '0'
        elif (si == '0' and s > 0) or t <= 0:
            ans[i] = si
            s -= 1
        else:
            ans[i] = ti
            t -= 1
    return print(*ans, sep='')


if __name__ == '__main__':
    N = int(input())
    S, T = input(), input()

    main()
