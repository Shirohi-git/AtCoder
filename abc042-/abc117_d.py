n, k = map(int, input().split())
a = list(map(int, input().split()))

bit = [0] * 40
for i in range(40):
    tmp = sum((ai >> i) & 1 for ai in a)
    bit[i] = ((n - 2 * tmp) * (2 << i), i)

x = 0
for num, i in sorted(bit)[::-1]:
    if num > 0 and x + (1 << i) <= k:
        x += (1 << i)
print(sum(ai ^ x for ai in a))
