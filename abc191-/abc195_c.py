n = int(input())

ans = 0
pow10 = [pow(10, i) for i in range(17)]
for i in range(len(str(n))):
    if pow10[i + 1] > n:
        exit(print(ans + i // 3 * (n - pow10[i] + 1)))
    ans += i // 3 * (pow10[i + 1] - pow10[i])
