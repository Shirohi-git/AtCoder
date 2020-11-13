s = input()

ans, cnt = 0, 0
for si in s:
    cnt = (cnt + 1) * (si in 'ATCG')
    ans = max(ans, cnt)
print(ans)
