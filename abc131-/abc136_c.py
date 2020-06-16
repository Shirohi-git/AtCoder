import sys

n = int(input())
h = list(map(int, input().split()))
max_h = 0
for i in h:
    if i < max_h:
        print('No')
        sys.exit()
    max_h = max(max_h, i-1)
print('Yes')
