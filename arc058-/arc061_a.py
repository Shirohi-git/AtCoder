from itertools import product

s = input()

ans = 0
for l in product([0, 1], repeat=len(s) - 1):
    num = s[0]
    for i, bit in enumerate(l):
        if bit == 0:
            num = ''.join([num, s[i + 1]])
        elif bit == 1:
            ans += int(num)
            num = s[i + 1]
    ans += int(num)
print(ans)
