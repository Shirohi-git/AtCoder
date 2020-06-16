from re import match
s, t = input().replace('?', '.'), input()

for i in range(len(s) - len(t) + 1)[::-1]:
    if match(s[i:i + len(t)], t):
        key = (s[:i] + t + s[i + len(t):]).replace('.', 'a')
        print(key)
        break
else:
    print('UNRESTORABLE')
