def main():
    from collections import defaultdict

    cnt = defaultdict(lambda: [])
    for i, ai in enumerate(A, 1):
        cnt[ai].append(i)
    
    for x, k in XK:
        ans = -1
        if len(cnt[x]) >= k:
            ans = cnt[x][k-1]
        print(ans)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    XK = [list(map(int, input().split())) for _ in range(Q)]

    main()
