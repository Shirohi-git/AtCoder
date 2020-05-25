s = str(input())

wlist = [i for i in range(len(s)) if s[i] == 'W']
ans, cnt = 0, 0
for i in wlist:
    ans += i - cnt
    cnt += 1
print(ans)
