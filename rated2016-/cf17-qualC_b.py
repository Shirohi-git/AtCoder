n = int(input())
a = list(map(int, input().split()))

cnt = 1
for ai in a:
    cnt *= 2 - (ai % 2)
print(pow(3, n) - cnt)
