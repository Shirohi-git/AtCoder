n, x = map(int, input().split())
s = input()

ans = x
for si in s:
    ans += (si == 'o') - (si == 'x')
    ans = max(ans, 0)
print(ans)
