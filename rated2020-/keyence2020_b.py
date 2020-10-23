n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]

ans, r = n, -(10 ** 9)
xlsort = sorted((x + l, x - l) for x, l in xl)
for ri, li in xlsort:
    ans -= (li < r)
    r += (ri - r) * (li >= r)
print(ans)
