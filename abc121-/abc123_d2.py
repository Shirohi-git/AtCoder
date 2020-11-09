from heapq import heappop, heappush

x, y, z, k = map(int, input().split())
a = sorted(map(int, input().split()))[::-1]
b = sorted(map(int, input().split()))[::-1]
c = sorted(map(int, input().split()))[::-1]

# 別解ver1 O(klogk)
hque = [(-a[0] - b[0] - c[0], 0, 0, 0)]
plus = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
frag = set([0])
for _ in range(k):
    ans, *cnt = heappop(hque)
    for d in plus:
        p, q, r = (ci + di for ci, di in zip(cnt, d))
        f = p + q * x + r * x * y
        if (f not in frag) and p < x and q < y and r < z:
            heappush(hque, (-a[p] - b[q] - c[r], p, q, r))
            frag.add(f)
    print(-ans)
