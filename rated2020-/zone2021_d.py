from collections import deque

s = input()

t = deque([])
cnt = 0
for si in s:
    if si == 'R':
        cnt ^= 1
    elif cnt:
        if t and t[0] == si:
            t.popleft()
        else:
            t.appendleft(si)
    else:
        if t and t[-1] == si:
            t.pop()
        else:
            t.append(si)
print(*list(t)[::-1] if cnt else t, sep='')
