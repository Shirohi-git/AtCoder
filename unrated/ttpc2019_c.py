n, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = x
for i in range(n):
    if a[i] != -1:
        cnt = cnt ^ a[i]
for i in range(n):
    if a[i] == -1:
        a[i] = cnt
        while a[i] > x:
            z = 2**(a[i].bit_length()-1)
            a[i] -= z
        cnt = cnt ^ a[i]
if cnt != 0:
    print(-1)
else:
    print(*a)
