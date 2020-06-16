x, n = map(int, input().split())
p = set(map(int, input().split()))

if n == 0:
    print(x)
else:
    for i in range(101):
        if x - i not in p:
            print(x - i)
            break
        elif x + i not in p:
            print(x + i)
            break
