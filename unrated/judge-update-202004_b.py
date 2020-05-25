import sys
input = sys.stdin.readline


n = int(input())
xc = [list(map(str, input().split())) for _ in range(n)]
for i in range(n):
    xc[i][0] = int(xc[i][0])
xc.sort(key=lambda x: x[0])
xc.sort(key=lambda x: x[1], reverse=True)

for i in range(n):
    print(xc[i][0])
