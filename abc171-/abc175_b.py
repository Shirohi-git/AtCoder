n = int(input())
l = sorted(map(int, input().split()))[::-1]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if l[k] < l[j] < l[i] < l[k] + l[j]:
                ans += 1
print(ans)
