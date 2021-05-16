from collections import Counter

n = int(input())
a = list(map(int, input().split()))

tmp = 1
acc = [0]
for ai in a:
    acc.append(acc[-1] + tmp * ai)
    tmp *= -1

ans = 0
cnt = Counter(acc)
for v in cnt.values():
    ans += v * (v-1) // 2
print(ans)
