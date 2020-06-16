import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort(reverse=True)
n_h = h[k:]
print(sum(n_h))