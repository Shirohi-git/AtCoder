s = input()[::-1]
d = {'maerd', 'remaerd', 'esare', 'resare'}

cnt = 0
while cnt < len(s):
    if s[cnt:cnt + 5] in d:
        cnt += 5
    elif s[cnt:cnt + 6] in d:
        cnt += 6
    elif s[cnt:cnt + 7] in d:
        cnt += 7
    else:
        print('NO')
        break
else:
    print('YES')
