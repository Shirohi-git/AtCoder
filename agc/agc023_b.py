def solve(num):
    for i in range(n):
        for j in range(i, n):
            if s[i - num][j] != s[j - num][i]:
                return 0
    return 1

# 解説AC
n = int(input())
s = [input() for _ in range(n)]

ans = 0
for k in range(n):
    ans += solve(k)
print(ans * n)
