n, m = map(int, input().split())
a = list(map(int, input().split()))

# 解説AC O(n) ver.2 #公式解説
pos = [[-1] for _ in range(n + 1)]
for i, ai in enumerate(a):
    pos[ai].append(i)

for num, lst in enumerate(pos):
    if any(q - p > m for p, q in zip(lst, lst[1:] + [n])):
        exit(print(num))
