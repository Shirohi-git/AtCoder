from collections import Counter

n = input()

k, ans, mod = len(n), -1, int(n) % 3
cnt = Counter(map(lambda x: int(x) % 3, n))
for num, res in zip([3 - mod, mod], [2, 1]):
    if cnt[num] >= res and k > res:
        ans = res
print(ans * (mod > 0))
