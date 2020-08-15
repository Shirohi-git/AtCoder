n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

frag, loop, lsum = set(), [], []
for i in range(n):
    if i in frag:
        continue
    now, tmpl, tmps = i, [], 0
    while (now not in frag):
        frag.add(now), tmpl.append(now)
        now = p[now] - 1
        tmps += c[now]
    else:
        loop.append(tmpl * 2)
        lsum.append(tmps)

lacc = []
for l in loop:
    tmp = [0]
    for li in l[1:]: 
        tmp.append(tmp[-1] + c[li])
    lacc.append(tmp)

ans = min(c)
for l, la, ls in zip(loop, lacc, lsum):
    llen = len(l) // 2
    for cnt in range(1, min(llen, k) + 1):
        for i in range(len(l) - cnt - 1):
            tmp = la[i + cnt] - la[i]
            tmp2 = ls * (k // llen - (cnt > k % llen))
            ans = max(ans, tmp, tmp + tmp2)
print(ans)
