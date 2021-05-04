h, w, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

pro = [(i-1, j-1) for i in range(3) for j in range(3)]
dic, lst = set(), set()
for ai, bi in ab:
    dic.add((ai, bi))
    lst |= set((ai+p, bi+q) for p, q in pro)

ans = [(h-2) * (w-2)] + [0] * 9
for x, y in lst:
    if 1 < x < h and 1 < y < w:
        cnt = sum((x+p, y+q) in dic for p, q in pro)
        ans[0] -= 1
        ans[cnt] += 1
print(*ans, sep='\n')
