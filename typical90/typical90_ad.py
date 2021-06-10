def main():
    ans = 0
    cnt = [0 for _ in range(N + 1)]
    for i in range(2, N + 1):
        if cnt[i] < 1:
            for j in range(i, N + 1, i):
                cnt[j] += 1
        ans += (cnt[i] >= K)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    main()
