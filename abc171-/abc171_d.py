from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]

ans = sum(a)
a = Counter(a)
for b, c in bc:
    ans += (c - b) * a[b]
    a[c] += a[b]
    a[b] = 0
    print(ans)
