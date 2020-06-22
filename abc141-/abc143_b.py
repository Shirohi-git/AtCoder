from itertools import combinations
n = int(input())
d = list(map(int, input().split()))

cnt = 0
for i, j in combinations(d, 2):
    cnt += i * j
print(cnt)
