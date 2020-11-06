n = int(input())
h = list(map(int, input().split()))

ans, hmax = 0, 0
for hi in h:
    ans += (hmax <= hi)
    hmax = max(hmax, hi)
print(ans)
