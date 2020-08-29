s, t = input(), input()

ans = len(t)
for i in range(len(s) - len(t) + 1):
    cnt = sum(si != ti for si, ti in zip(s[i:i + len(t)], t))
    ans = min(cnt, ans)
print(ans)
