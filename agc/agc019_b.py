from collections import Counter

a = input()
cnta = Counter(a)

ans = (len(a)** 2 - len(a)) // 2 + 1
for i in cnta.values():
    ans -= (i ** 2 - i) // 2
print(ans)
