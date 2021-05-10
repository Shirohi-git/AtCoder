from heapq import heapify, heappop, heappush

k, n, m = map(int, input().split())
a = list(map(int, input().split()))

# 解法2 O(klogk) 
b = [m * ai // n for ai in a]
que = [(n * b[i] - m * a[i], i) for i in range(k)]
heapify(que)

cnt = sum(b)
while cnt < m:
    tmp, idx = heappop(que)
    cnt += 1
    b[idx] += 1
    heappush(que, (tmp + n, idx))
print(*b)
