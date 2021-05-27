def main():
    dp = [[1e6] * n for _ in range(26)]
    for i in range(n):
        dp[ord(s[i])-ord('a')][i] = i
    for j in range(n-2, -1, -1):
        for dpi in dp:
            if dpi[j] == 1e6:
                dpi[j] = dpi[j+1]

    ans = [''] * k
    idx = 0
    for j in range(k):
        for dpi in dp:
            if n-1 - dpi[idx] >= k-1 - j:
                idx = dpi[idx] + 1
                ans[j] = s[idx-1]
                break
    print(*ans, sep='')


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    main()
