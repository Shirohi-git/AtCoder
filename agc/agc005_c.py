from collections import Counter

n = int(input())
a = list(map(int, input().split()))

ma = max(a)
cnt = Counter(a)
res = all(cnt[i+1] >= 2 for i in range((ma+1) // 2, ma))
res &= (cnt[ma//2 + ma % 2] == 1 + ma % 2)
print('Possible' if res else 'Impossible')
