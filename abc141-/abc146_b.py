n = int(input())
s = list(input())

for i in range(len(s)):
    tmp = ord(s[i]) + n
    if tmp >= 91:
        tmp = tmp - 26
    s[i] = chr(tmp)

print(*s, sep='')
