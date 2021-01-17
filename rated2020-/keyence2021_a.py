n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c, maxa = 0, 0
for ai, bi in zip(a, b):
    maxa = max(maxa, ai)
    c = max(c, maxa * bi)
    print(c)
