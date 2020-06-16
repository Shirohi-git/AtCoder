s = list(input())
s_f = s[0: (len(s) - 1) // 2]
s_b = s[(len(s) + 3) // 2 - 1: len(s)]

if (s != s[::-1]) or (s_f != s_f[::-1]) or (s_b != s_b[::-1]):
    print('No')
else:
    print('Yes')
