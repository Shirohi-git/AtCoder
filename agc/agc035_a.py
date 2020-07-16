from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))

cnt = 0
for i in a:
    cnt ^= i

if n % 3 == 0 and all(a[i] % (n // 3) == 0 for i in a):
    print('Yes' if (cnt == 0 or a[0] == n // 3) else 'No')
else:
    print('Yes' if a[0] == n else 'No')
