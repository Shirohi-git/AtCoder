n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans, cnt = 0, -sum(ai for ai, _ in ab)
for num in sorted(-2 * ai - bi for ai, bi in ab):
    if cnt > 0:
        break
    cnt -= num
    ans += 1
print(ans)
