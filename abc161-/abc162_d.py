from itertools import product as pro

n = int(input())
s = str(input())

r = [i for i in range(n) if s[i] == 'R']
g = [i for i in range(n) if s[i] == 'G']
b = [i for i in range(n) if s[i] == 'B']
cnt = len(r) * len(g) * len(b)

length = max(len(r), len(g), len(b))
for i, j, k in [(r, g, b), (g, b, r), (b, r, g)]:
    if length == len(i):
        max1 = set(i)
        min1, min2 = j, k

for i, j in pro(min1, min2):
    if 2*j-i in max1:
        cnt -= 1
    if 2*i-j in max1:
        cnt -= 1
    if (i+j)/2 in max1:
        cnt -= 1

print(cnt)