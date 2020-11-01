from bisect import bisect

n, m = map(int, input().split())
h = sorted(map(int, input().split()))
w = sorted(map(int, input().split()))

front, back = [0], [0]
for i in range(1, n, 2):
    front.append(h[i] - h[i - 1] + front[-1])
    back.append(h[i + 1] - h[i] + back[-1])

ans = float('inf')
for wi in w:
    num = bisect(h, wi)
    tmp = front[num // 2] + back[-1] - back[num // 2]
    ans = min(ans, tmp + abs(wi - h[num - (num % 2)]))
print(ans)
