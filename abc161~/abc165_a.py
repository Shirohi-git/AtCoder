n = int(input())
a, b = map(int, input().split())
if (a <= b//n*n)and(b//n*n <= b):
    print('OK')
else:
    print('NG')
