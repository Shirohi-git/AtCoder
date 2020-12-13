n, m = map(int, input().split())
a = [0] + sorted(map(int, input().split())) + [n + 1]

if n == m:
    exit(print(0))

diff = []
for i in range(m + 1):
    tmp = a[i + 1] - a[i] - 1
    if tmp > 0:
        diff.append(tmp)
k = min(diff)

ans = sum((d + k - 1) // k for d in diff)
print(ans)
