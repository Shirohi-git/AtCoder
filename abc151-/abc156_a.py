import sys
input = sys.stdin.readline


n, r = map(int, input().split())

if n < 10:
    print(100*(10-n)+r)
else:
    print(r)
