n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

ans = sum(abs(ai-bi) for ai, bi in zip(a, b))
print(ans)
