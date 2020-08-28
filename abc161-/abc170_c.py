x, n = map(int, input().split())
p = set(map(int, input().split()))

ans = min(abs(x - i) for i in range(102) if i not in p)
print(x + ans if (x - ans in p) else x - ans)
