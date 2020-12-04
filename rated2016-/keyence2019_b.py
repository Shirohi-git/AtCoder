s = input()

res = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        tmp = s[:i] + s[j:]
        res |= (tmp == 'keyence')
print('YES' if res else 'NO')
