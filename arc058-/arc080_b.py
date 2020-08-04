h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

l = []
for i, ai in enumerate(a, 1):
    l += [i] * ai

for i in range(h):
    ansi = l[w * i:w * (i + 1)]
    print(*(ansi if i % 2 == 0 else ansi[::-1]))
