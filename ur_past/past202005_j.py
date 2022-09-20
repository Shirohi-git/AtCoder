def binary(N,A,LIST):
    l, r = -1, N
    while r - l > 1:
        if LIST[(l + r) // 2] < A:
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r + 1

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * n

for i in a:
    ans = binary(n, i, cnt)
    if ans <= n:
        cnt[ans - 1] = i
        print(ans)
    else:
        print(-1)
