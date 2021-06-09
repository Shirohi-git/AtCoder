def main():
    cnt = [0 for _ in range(N + 1)]
    for i in range(2, N + 1):
        if cnt[i] > 0:
            continue
        for j in range(i, N + 1, i):
            cnt[j] += 1
    ans = sum(ci >= K for ci in cnt)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    main()
