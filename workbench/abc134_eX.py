from heapq import heappop, heappush

n = int(input())
a = [int(input()) for _ in range(n)]

h = [a[0]]
for ai in a[1:]:
    tmp = heappop(h)
    if tmp >= ai:
        heappush(h, ai)
        heappush(h, tmp)
    elif tmp < ai:
        heappush(h, ai)
    print(h)
print(len(h))
