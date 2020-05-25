n = int(input())

cnt=[[0,0,0,0,0,0,0,0,0,0] for _ in range(10)]
ans = 0


for i in range(n+1):
    i = list(str(i))
    cnt[int(i[0])][int(i[-1])] += 1

for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
