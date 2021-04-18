n = int(input())
a = sorted(set(map(int, input().split())))[::-1] + [0]
MOD1 = 10 ** 9 + 7

ans = 1
for ai, aj in zip(a, a[1:]):
    ans *= ai - aj + 1
    ans %= MOD1
print(ans)
