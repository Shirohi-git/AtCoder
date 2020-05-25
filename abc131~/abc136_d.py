s = str(input())
a = [1 if i == 'R' else - 1 for i in s] + [0]
ans = [0] * len(s)

lhigh, llow, rlow, rhigh = 0, 0, 0, 0
for i in range(len(s)):
    if a[i + 1] + 2 == a[i]:  # 1,-1
        llow = i
        rlow = i + 1
    elif (a[i + 1] - 2 == a[i]) or (i == len(s) - 1):
        rhigh = i
        lcnt, rcnt = llow - lhigh + 1, rhigh - rlow + 1
        ans[llow] = lcnt // 2 + rcnt // 2 + lcnt % 2
        ans[rlow] = lcnt // 2 + rcnt // 2 + rcnt % 2
        lhigh = i + 1
print(*ans)
