n = int(input())
h = list(map(int, input().split())) + [0]

ans, cnt = 0, sum(h)
while cnt > 0:
    l, r = -1, n
    for num, i in enumerate(h):
        if (l == -1) and (i > 0):
            l = num
        if (l > -1) and (i == 0):
            r = num
            ans += 1
            cnt -= r - l
            for i in range(l, r):
                h[i] -= 1
            break
print(ans)
