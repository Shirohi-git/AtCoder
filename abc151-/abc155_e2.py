n = list(map(int, reversed('0' + input())))

ans, up = 0, 0
for i in range(len(n) - 1):
    cnt, up = up + n[i], 0
    if (cnt > 5) or (cnt == 5 and n[i + 1] >= 5):
        cnt, up = 10 - cnt, 1
    ans += cnt
print(ans + up)
