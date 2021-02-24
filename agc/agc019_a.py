q, h, s, d = map(int, input().split())
n = int(input())

s = min(q * 4, h * 2, s)
ans = s * (n % 2) + min(s * 2, d) * (n // 2)
print(ans)
