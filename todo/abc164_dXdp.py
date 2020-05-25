import sys
s = str(input())

cnt = [0 for i in range(len(s))]

if len(s) < 5:
    print(sum(cnt))
    sys.exit()

for i in range(len(s)-3):
    for j in range(i+4, min(len(s), i+10)):
        if int(s[i:j+1]) % 2019 == 0:
            cnt[j] += cnt[i-1] + 1
else:
    print(sum(cnt))
