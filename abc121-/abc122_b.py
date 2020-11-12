s = input()

ans, cnt = 0, 0
for si in s:
    cnt *= (si in 'ATCG')
    cnt += (si in 'ATCG')
    ans = max(ans, cnt)
print(ans)
