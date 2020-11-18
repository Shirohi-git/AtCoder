s = input()

ans, cnt = 0, 0
for si in s:
    if cnt == 1 and (si in [',', ':', '}']):
        ans |= (si == ':') | (s == '{}')
        exit(print('dict' if ans else 'set'))
    cnt += (si == '{') - (si == '}')
