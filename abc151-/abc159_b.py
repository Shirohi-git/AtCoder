s = input()
s1, s2 = s[:(len(s) - 1) // 2], s[(len(s) + 1) // 2:]

ans = (s1 == s1[::-1] == s2)
print('Yes' if ans else 'No')
