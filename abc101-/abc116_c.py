n = int(input())
h = list(map(int, input().split())) + [0]

ans, cnt = 0, sum(h)
while cnt > 0:
    l, r = -1, n
    for i, hi in enumerate(h):
        if l == -1 and hi > 0:
            l = i
        if l > -1 and hi == 0:
            r = i
            ans += 1
            cnt -= r - l
            for j in range(l, r):
                h[j] -= 1
            break
print(ans)
