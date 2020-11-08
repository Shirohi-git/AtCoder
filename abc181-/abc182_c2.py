from itertools import combinations

# 解説別ver.
n = list(map(int, list(input())))
sumn, ans = sum(n), -1
for i in range(len(n))[::-1]:
    for c in combinations(n, i):
        if (sumn - sum(c)) % 3 == 0:
            ans = i
print(ans)
