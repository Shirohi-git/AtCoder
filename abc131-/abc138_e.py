from bisect import bisect_left as bisect

s, t = input(), input()
lens, sets = len(s), set(s)

if not all(i in sets for i in t):
    print(-1)
    exit()

alp = [[] for i in range(26)]
for i, si in enumerate(s):
    alp[ord(si) - 97].append(i)

ans, cnt = 1 - lens, 0
for i in t:
    li = alp[ord(i) - 97]
    ans += lens * (cnt == 0)
    num = bisect(li, cnt)
    ans += lens * (num == len(li))
    cnt = (li[num % len(li)] + 1) % lens
print(ans + (cnt - 1) % lens)
