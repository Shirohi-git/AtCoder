import heapq

n, m = map(int, input().split())
a = [-int(i) for i in input().split()]
heapq.heapify(a)
for i in range(m):
    b = heapq.heappop(a)//(-2)
    heapq.heappush(a,-b)
print(-sum(a))
