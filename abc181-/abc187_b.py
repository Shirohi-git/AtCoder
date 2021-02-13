n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i, (ax, ay) in enumerate(xy):
    for bx, by in xy[i + 1:]:
        cnt += sum(-1 <= (ay - by) / (ax - bx) <= 1)
print(cnt)
