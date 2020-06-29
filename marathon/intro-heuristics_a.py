d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]

last, infimum = [0] * 26, []
for di in range(d):
    minus = [c[i] * (di + 1 - last[i]) for i in range(26)]
    cnt = [s[di][i] + minus[i]  for i in range(26)]
    ti = cnt.index(max(cnt))
    last[ti] = di + 1
    infimum.append(ti + 1)
print(infimum)