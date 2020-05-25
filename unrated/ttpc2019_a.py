a, b, t = map(int, input().split())
ans = b
while t > ans:
    ans += b-a
print(ans)
