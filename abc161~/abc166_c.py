import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]

h_max = [0 for _ in range(n)]
for a, b in ab:
    h_max[a-1] = max(h_max[a-1], h[b-1])
    h_max[b-1] = max(h_max[b-1], h[a-1])

cnt = 0
for i in range(n):
    if h[i] > h_max[i]:
        cnt += 1
print(cnt)
