n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

dict = {'s': r, 'p': s, 'r': p}
cnt, ans = set(), 0
for i, ti in enumerate(t):
    if (i - k in cnt) and ti == t[i - k]:
        continue
    ans += dict[ti]
    cnt.add(i)
print(ans)
