from heapq import heappush, heappop

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

day = [[] for _ in range(10 ** 5)]
for a, b in ab:
    day[a - 1].append(b)

work, ans = [], 0
for i in range(m):
    for j in day[i]:
        heappush(work, -j)
    if len(work) > 0:
        ans -= heappop(work)
print(ans)
