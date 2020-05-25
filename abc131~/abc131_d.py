import sys
input = sys.stdin.readline

n = int(input())
ab = sorted([list(map(int, input().split()))[::-1] for _ in range(n)])

cnt = 0
for b, a in ab:
    cnt += a
    if cnt > b:
        print('No')
        break
else:
    print('Yes')
