import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

len_a = len(a)
set_a = len(set(a))

if len_a == set_a:
    print('YES')
else:
    print('NO')
