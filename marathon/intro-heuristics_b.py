d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

last = [0] * 26
ans = 0
for di in range(d):
    ans += s[di][t[di] - 1]
    last[t[di] - 1] = di + 1
    ans -= sum(c[i] * (di + 1 - last[i]) for i in range(26))
    print(ans)
