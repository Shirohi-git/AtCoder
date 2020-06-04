n = int(input())
p = list(map(int, input().split()))

ans, cnt = 0, 0
for i in range(1, n + 1):
    if i == p[i - 1]:
        cnt += 1
        if cnt % 2 == 1:
            ans += 1
    else:
        cnt = 0
print(ans)
