l = input()
MOD = 10 ** 9 + 7

pow3 = [1]
for i in range(len(l)):
    pow3.append(pow3[-1] * 3 % MOD)

ans, cnt = 0, 1
for i in range(len(l)):
    if l[i] == '1':
        ans += (pow3[len(l) - i - 1] * cnt) % MOD
        cnt = cnt * 2 % MOD
print((ans + cnt) % MOD)
