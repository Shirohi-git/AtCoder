n = int(input())
ab = [map(int, input().split()) for _ in range(n)]

ans = 0
for a, b in ab[::-1]:
    a += ans
    if a % b > 0:
        ans += b - (a % b)
print(ans)
