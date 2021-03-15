n = int(input())
s1, s2 = input() + '0', input() + '0'
MOD = 10**9 + 7

l1 = [s1[i] for i in range(n) if s1[i] != s1[i - 1]]
l2 = [s2[i] for i in range(n) if s2[i] != s2[i - 1]]

bfo = (l1[0] != l2[0])
ans = 3 + 3 * bfo
for l1i, l2i in zip(l1[1:], l2[1:]):
    now = (l1i != l2i)
    ans *= 2 + (bfo * (2 * now - 1))
    bfo, ans = now, ans % MOD
print(ans)
