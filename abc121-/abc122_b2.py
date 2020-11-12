from re import fullmatch

s = input()

ans = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if fullmatch('[ATCG]*', s[i:j + 1]):
            ans = max(ans, j + 1 - i)
print(ans)
