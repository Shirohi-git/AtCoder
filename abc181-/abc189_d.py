n = int(input())
s = [input() for _ in range(n)]

ans = 1
for i, si in enumerate(s):
    if si == 'OR':
        ans += pow(2, i + 1)
print(ans)
