r, g, b = map(int, input().split())
k = int(input())

for i in range(k):
    if r >= g:
        g *= 2
    elif g >= b:
        b *= 2
print('Yes' if r < g < b else 'No')
