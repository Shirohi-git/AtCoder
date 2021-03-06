n = int(input())

ans = -1
for i in range(n):
    ans += n / (n - i)
print(ans)
