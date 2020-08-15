x, k, d = map(int, input().split())

x, cnt = abs(x), abs(x) // d
if k % 2 == cnt % 2:
    ans = abs(x - d * min(k, cnt))
elif k % 2 != cnt % 2:
    ans = abs(x - d * min(k, cnt + 1))
print(ans)
