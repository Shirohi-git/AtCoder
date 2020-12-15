n, a, b = map(int, input().split())
v = sorted(map(int, input().split()))[::-1]

ave = sum(v[:a]) / a
print(ave)

cntl = v[:a].count(v[a - 1])
cnt = v[a:].count(v[a - 1]) + cntl
fact = [1, 1]
for i in range(2, cnt + 1):
    fact.append(fact[-1] * i)

ans, l = 0, cntl
r = min(l + (b - a) * (v[0] == v[a - 1]), cnt)
for i in range(l, r + 1):
    ans += fact[cnt] // fact[i] // fact[cnt - i]
print(ans)
