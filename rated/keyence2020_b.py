import sys
input = sys.stdin.readline

n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
xl2 = sorted([[x + l, x - l] for x, l in xl])

ans = 0
mr = xl2[0][1]
for r, l in xl2:
    if l >= mr:
        ans += 1
        mr = r
print(ans)
