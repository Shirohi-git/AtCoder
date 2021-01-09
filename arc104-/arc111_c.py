n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = [pi - 1 for pi in map(int, input().split())]

if any(b[p[i]] >= a[i] and i != p[i] for i in range(n)):
    exit(print(-1))
que = sorted((-a[i], i) for i in range(n) if i != p[i])

ans = []
for _, now in que:
    while p[now] != now:
        pnow = p[now]
        ans.append((now + 1, pnow + 1))
        p[pnow], p[now] = p[now], p[pnow]
print(len(ans))
for swap in ans:
    print(*swap)
