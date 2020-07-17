s = input()

brk = 0
for i in s:
    if i == '{':
        brk += 1
    elif i == '}':
        brk -= 1
    if brk == 1:
        if i == ':':
            print('dict')
            exit()
        elif i == ',':
            print('set')
            exit()
else:
    if s == '{}':
        print('dict')
    else:
        print('set')
