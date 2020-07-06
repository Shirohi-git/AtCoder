n = int(input())
uv = [sorted(map(int, input().split())) for _ in range(n - 1)]

# 解説AC
ans = sum(i * (n + 1 - i) for i in range(n + 1))
for u, v in uv:
    ans -= u * (n - v + 1)
print(ans)
