n = int(input())
l = list(map(int, input().split()))

sl = sorted(l)
a, b = sl[n // 2 - 1], sl[n // 2]
for i in l:
    if i <= a:
        print(b)
    else:
        print(a)
