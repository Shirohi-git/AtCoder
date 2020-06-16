from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

l = [i for i in range(1, m+1)]
ans = 0
for Alis in combinations_with_replacement(l, n):
    cnt = 0
    for i in range(q):
        if Alis[abcd[i][1] - 1] - Alis[abcd[i][0] - 1] == abcd[i][2]:
            cnt += abcd[i][3]
    ans = max(ans, cnt)

print(ans)
