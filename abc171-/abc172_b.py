s, t = input(), input()

cnt = 0
for si, ti in zip(s, t):
    if si != ti:
        cnt += 1
print(cnt)
