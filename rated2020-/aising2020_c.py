n = int(input())

cnt = [0] * n
for x in range(1, int(n ** 0.5) + 1):
    for y in range(1, int(n ** 0.5) + 1):
        for z in range(1, int(n ** 0.5) + 1):
            num = (x + y) ** 2 - x * y + z * (x + y + z)
            if num <= n:
                cnt[num - 1] += 1
print(*cnt, sep="\n")
