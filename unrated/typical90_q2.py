n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

if n > 1000:
    exit()

# 小課題2 O(n2)
out = [[0] * n for i in range(n)]
for l, r in lr:
    out[l-1][r-1] = 1

ans = 0
lst = [0] * n
for i in range(n):
    sumout, lst[i] = sum(out[i]), 0
    for j in range(n):
        sumout -= out[i][j]
        ans += sumout * lst[j]
        lst[j] += out[i][j]
print(ans)
