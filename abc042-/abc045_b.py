strin = [input(), input(), input()]

l = ['a','b','c']
cnt, nxt = [0, 0, 0], 0
while True:
    lttr = strin[nxt][cnt[nxt]]
    cnt[nxt] += 1
    nxt = l.index(lttr)
    if cnt[nxt] >= len(strin[nxt]):
        print(l[nxt].upper())
        break
