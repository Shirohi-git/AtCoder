n = int(input())
p = list(map(int, input().split()))

ans, cnt = n, n + 1
for pi in p:
    ans -= (cnt < pi)
    cnt = min(cnt, pi)
print(ans)
