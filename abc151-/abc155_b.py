import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in a:
    if i % 2 == 0:
        if (i % 3 == 0) | (i % 5 == 0):
            pass
        else:
            cnt = 1

if cnt == 1:
    print('DENIED')
else:
    print('APPROVED')
