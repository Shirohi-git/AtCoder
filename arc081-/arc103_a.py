from collections import Counter

n = int(input())
v = list(map(int, input().split()))

even = [v[i] for i in range(n) if i % 2 == 0]
odd = [v[i] for i in range(n) if i % 2 == 1]
ecnt = Counter(even).most_common() + [(0, 0)]
ocnt = Counter(odd).most_common() + [(0, 0)]

if ecnt[0][0] == ocnt[0][0]:
    print(n - max(ecnt[0][1] + ocnt[1][1], ecnt[1][1] + ocnt[0][1]))
else:
    print(n - ecnt[0][1] - ocnt[0][1])
