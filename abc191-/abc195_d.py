n, m, q = map(int, input().split())
wv = [list(map(int, input().split())) + [i] for i in range(n)]
x = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]

wv = sorted(wv, key=lambda x: x[1])
for l, r in query:
    ans, cnt = 0, [1] * n
    for box in sorted(x[:l - 1] + x[r:]):
        tmp = [(v, i) for w, v, i in wv if cnt[i] and w <= box]
        if tmp:
            val, idx = max(tmp)
            ans, cnt[idx] = ans + val, 0
    print(ans)
