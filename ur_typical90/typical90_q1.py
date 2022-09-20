n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

if m > 1000:
    exit()

# 小課題1 O(m2)
ans = 0
for li, ri in lr:
    for lj, rj in lr:
        ans += (li < lj < ri < rj)
print(ans)
