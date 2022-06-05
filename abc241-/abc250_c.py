def main():
    ans = [i+1 for i in range(N)]
    dic = [i for i in range(N)]
    
    for x in X:
        now = dic[x-1]
        nxt = (now+1 if now != N-1 else now-1)
        dic[x-1], dic[ans[nxt]-1] = nxt, now
        ans[now], ans[nxt] = ans[nxt], ans[now]
    return print(*ans)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]

    main()
