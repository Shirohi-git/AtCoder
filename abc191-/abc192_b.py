s = input()

odd, evn = s[::2], s[1::2]
res = (odd + 'a').islower() and (evn + 'A').isupper()
print('Yes' if res else 'No')
