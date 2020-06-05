from fractions import gcd

n = int(input())
a = list(map(int, input().split()))

fgcd, ftmp = [], a[0]
for i in a:
    ftmp = gcd(ftmp, i)
    fgcd.append(ftmp)

bgcd, btmp = [], a[-1]
for i in a[::-1]:
    btmp = gcd(btmp, i)
    bgcd.append(btmp)
bgcd = bgcd[::-1]

egcd = [bgcd[1]] + [0] * (n - 2) + [fgcd[n - 2]]
for i in range(1, n - 1):
    egcd[i] = gcd(fgcd[i - 1], bgcd[i + 1])
print(max(egcd))
