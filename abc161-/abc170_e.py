from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(q)]

thq = []
top = defaultdict(int)
topcnt = defaultdict(int)
rhq = [[] for _ in range(2 * 10 ** 5 + 1)]
rate = [defaultdict(int) for _ in range(2 * 10 ** 5 + 1)]
for a, b in ab:
    top[b] = max(top[b], a)
    rate[b][a] += 1
    heapq.heappush(rhq[b], -a)
for num in top.values():
    heapq.heappush(thq, num)
    topcnt[num] += 1

for c, d in cd:
    a, b = ab[c - 1]
    ab[c - 1][1] = d

    # 元の園について
    rate[b][a] -= 1
    if rate[b][a] == 0:
        del rate[b][a]
    topcnt[top[b]] -= 1
    if topcnt[top[b]] == 0:
        del topcnt[top[b]]
    del top[b]
    if len(rate[b]) > 0:
        top[b] = -heapq.heappop(rhq[b])
        while top[b] not in rate[b]:
            top[b] = -heapq.heappop(rhq[b])
        heapq.heappush(rhq[b], -top[b])
        heapq.heappush(thq, top[b])
        topcnt[top[b]] += 1

    # 新しい園について
    rate[d][a] += 1
    heapq.heappush(rhq[d], -a)
    if a > top[d]:
        if top[d] > 0:
            topcnt[top[d]] -= 1
            if topcnt[top[d]] == 0:
                del topcnt[top[d]]
        top[d] = a
        topcnt[top[d]] += 1
        heapq.heappush(thq, top[d])

    # 最小値について
    ans = heapq.heappop(thq)
    while ans not in topcnt:
        ans = heapq.heappop(thq)
    heapq.heappush(thq, ans)
    print(ans)
