n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])

fast, cnt, ans = 0, 0, 0
for i in t:
    if fast + k < i or cnt == c:
        cnt = 0
    if cnt == 0:
        ans += 1
        fast = i
    cnt += 1
print(ans)
