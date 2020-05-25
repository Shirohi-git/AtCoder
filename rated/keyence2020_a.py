h=int(input())
w = int(input())
n = int(input())

x = max(h, w)
if n % x == 0:
    print(n // x)
else:
    print(n//x+1)