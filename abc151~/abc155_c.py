n = int(input())
s = [str(input()) for _ in range(n)]
s.append('zzzzzzzzzzz')
s.sort()

l_cnt = []
c_max = 1
cnt = 1
bfo = 'xxxxxxxxxxx'

for i in s:
    if i == bfo:
        cnt += 1
        c_max = max(c_max, cnt)
    else:
        l_cnt.append([bfo, cnt])
        bfo = i
        cnt = 1

for j in range(len(l_cnt)):
    if j == 0:
        continue
    else:
        if c_max == l_cnt[j][1]:
            print(l_cnt[j][0])
