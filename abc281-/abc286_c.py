def main():
    s = S*2
    ans = INF
    for i in range(N):
        si = s[i:i+N]
        res = sum(B * (si[j] != si[N-1-j]) for j in range(N//2))
        ans = min(ans, res + A*i)
    return print(ans)


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    S = input()
    INF = 10**15

    main()
