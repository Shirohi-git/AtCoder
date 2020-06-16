from collections import deque

s = deque(list(str(input())))
q = int(input())
que = [list(map(str, input().split())) for _ in range(q)]

r_cnt=0
for query in que:
    if len(query) == 1:
        r_cnt+=1
    else:
        if int(query[1]) == 1:
            if r_cnt % 2 == 1:
                s.append(query[2])
            else:
                s.appendleft(query[2])
        else:
            if r_cnt % 2 == 1:
                s.appendleft(query[2])
            else:
                s.append(query[2])

for _ in range(r_cnt % 2):
    s.reverse()

print(*s,sep='')
