from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(q)]

m = 2 * 10 ** 5
thq = []
top = defaultdict(int)
rhq = [[] for _ in range(m + 1)]
rate = [defaultdict(int) for _ in range(m + 1)]
for a, b in ab:
    top[b] = max(top[b], a)
    rate[b][a] += 1
    heapq.heappush(rhq[b], -a)
    heapq.heappush(thq, top[b])

for c, d in cd:
    a, b = ab[c - 1]
    ab[c - 1][1] = d

    rate[b][a] -= 1
    if rate[b][a] == 0:
        del rate[b][a]
    del top[b]
    if len(rate[b]) > 0:
        top[b] = -heapq.heappop(rhq[b])
        while top[b] not in rate[b]:
            top[b] = -heapq.heappop(rhq[b])
        heapq.heappush(rhq[b], -top[b])
        heapq.heappush(thq, top[b])

    rate[d][a] += 1
    heapq.heappush(rhq[d], -a)
    top[d] = max(top[d], a)
    heapq.heappush(thq, top[d])

    ans = heapq.heappop(thq)
    while ans not in top.values():
        ans = heapq.heappop(thq)
    heapq.heappush(thq, ans)
    print(ans)
