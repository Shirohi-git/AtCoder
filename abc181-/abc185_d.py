n, m = map(int, input().split())
a = [0] + sorted(map(int, input().split())) + [n + 1]

diff = []
for i in range(m + 1):
    tmp = a[i + 1] - a[i] - 1
    if tmp > 0:
        diff.append(tmp)
ans, k = 0, min(diff + [n])
ans += sum((d + k - 1) // k for d in diff)
print(ans)
