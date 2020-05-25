import sys
input = sys.stdin.readline

n = int(input())
d = sorted(map(int, input().split()))

print(d[n//2] - d[n//2-1])
