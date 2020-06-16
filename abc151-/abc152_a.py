import sys
input = sys.stdin.readline


n, m = map(int, input().split())
if n == m:
    print('Yes')
else:
    print('No')