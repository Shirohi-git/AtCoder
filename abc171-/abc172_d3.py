n = int(input())

# O(n**0.5)
ans = 0
for i in range(1, int(n ** 0.5) + 1):
    cnt = ((n // i) * (n // i + 1) // 2) - (i * (i + 1) // 2)
    ans += i * cnt * 2 + i ** 2
print(ans)
