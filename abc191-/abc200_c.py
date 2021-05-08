from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter([ai % 200 for ai in a])
ans = 0
for k, v in cnt.items():
    ans += v * (v-1) // 2
print(ans)
