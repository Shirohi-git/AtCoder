n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

cnt, ans = set(), 0
for i, ti in enumerate(t):
    if (i - k in cnt) and ti == t[i - k]:
        continue
    ans += r * (ti == 's')
    ans += s * (ti == 'p')
    ans += p * (ti == 'r')
    cnt.add(i)
print(ans)
