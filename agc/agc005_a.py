x = input()

s, t = 0, 0
for i in x:
    if i == 'S':
        s += 1
    elif i == 'T':
        if s > 0:
            s -= 1
        else:
            t += 1
print(s + t)
