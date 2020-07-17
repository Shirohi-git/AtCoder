n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

red, cnt = set([1]), {i: 1 for i in range(1, n + 1)}
for xi, yi in xy:
    if xi in red:
        red.add(yi)
        if cnt[xi] == 1:
            red.remove(xi)
    cnt[xi] -= 1
    cnt[yi] += 1
print(len(red))
