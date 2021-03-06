from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
a = list(map(int, input().split()))

flag = [0] * (max(a) + 2)
for ai in a[:m]:
    flag[ai] += 1

heap = list(range((max(a) + 2)))
ans = num = flag.index(0)
for out, add in zip(a[:-m], a[m:]):
    flag[out] -= 1
    flag[add] += 1
    if flag[out] == 0:
        heappush(heap, out)
        num += (out - num) * (out < num)
    while flag[num] > 0:
        num = heappop(heap)
    ans = min(ans, num)
print(ans)
