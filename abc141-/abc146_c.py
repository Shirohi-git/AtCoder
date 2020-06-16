import sys

a, b, x = map(int, input().split())
if a * (10 ** 9) + b * len(str(10 ** 9)) <= x:
    print(10 ** 9)
    exit()

l, r = 0, 10 ** 9
for i in range(30):
    tmp = (r+l)//2
    if a * tmp + b * len(str(tmp)) <= x:
        l = tmp
    else:
        r = tmp
print(l)
