def main():
    ans, cnt, l = 0, 0, 0
    dic = {ai: 0 for ai in A}
    for r in range(N):
        if dic[A[r]] == 0:
            cnt += 1
        dic[A[r]] += 1
        while cnt > K:
            dic[A[l]] -= 1
            if dic[A[l]] == 0:
                cnt -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
