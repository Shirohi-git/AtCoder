n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

xy1 = max(x + y for x, y in xy)
xy2 = max(-x - y for x, y in xy)
xy3 = max(-x + y for x, y in xy)
xy4 = max(x - y for x, y in xy)

print(max(xy1 + xy2, xy3 + xy4))
