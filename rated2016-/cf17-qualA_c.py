from collections import Counter

h, w = map(int, input().split())
a = Counter(''.join(input() for _ in range(h)))

center = h * w % 2
side = (h // 2) * (w % 2) + (w // 2) * (h % 2)

if sum(a[i] % 2 for i in a) != center:
    print('No')
    exit()
a = {i: a[i] - (a[i] % 2) for i in a}
cnt = sum(a[i] % 4 == 2 for i in a)
print('Yes' if cnt <= side else 'No')
