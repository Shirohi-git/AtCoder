def main():
    p, ans = P[:], []
    for i in range(N):
        now = i
        while now > 1 and p[now-2] % 2 != now % 2 == p[now] % 2:
            p[now-2], p[now] = p[now], p[now-2]
            ans.append(['B', now-1])
            now -= 2

    for i in range(N-1):
        if p[i] % 2 == i % 2:
            p[i], p[i+1] = p[i+1], p[i]
            ans.append(['A', i+1])

    for i in range(N):
        idx = p.index(i+1)
        while idx != i:
            ans.append(['B', idx-1])
            p[idx], p[idx-2] = p[idx-2], p[idx]
            idx -= 2

    print(len(ans))
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    main()
