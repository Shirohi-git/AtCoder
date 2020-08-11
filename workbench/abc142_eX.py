import sys
input = sys.stdin.readline

n, m = map(int, input().split())
abc = []
for i in range(m):
    a, b = map(int, input().split())
    c = set(map(int, input().split()))
    abc.append([a,b,c])
