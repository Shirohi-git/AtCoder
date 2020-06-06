n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s = int(input())
k = int(input())
t = list(map(int, input().split()))

near = [[] for _ in range(n)]
for i, j in uv:
    near[i - 1].append(j - 1)
    near[j - 1].append(i - 1)

print(m)
