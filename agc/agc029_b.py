from collections import Counter

n = int(input())
a = [0] + sorted(map(int, input().split()))

cnta = Counter(a)
pow2 = [1]
for i in range(40):
    pow2.append(pow2[-1] * 2)

ans, num = 0, a.pop()
for pi in pow2[::-1]:
    while pi * 2 > num >= pi:
        pair = pi * 2 - num
        if pair == num:
            if cnta[num] >= 2:
                cnta[num] -= 2
                ans += 1
        elif cnta[pair] * cnta[num] > 0:
            cnta[pair] -= 1
            cnta[num] -= 1
            ans += 1
        num = a.pop()
print(ans)
