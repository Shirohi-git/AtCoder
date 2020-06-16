n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
while n > 1:
    n -= m - 1
    ans += 1
print(ans)
