n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    mini = a[i]
    for j in range(i, n):
        mini = min(mini, a[j])
        ans = max(mini * (j + 1 - i), ans)
print(ans)
