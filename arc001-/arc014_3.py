from collections import deque

n, s = int(input()), input() + '#'

que = deque([])
for i in range(n):
    if len(que) == 0:
        que.append(s[i])
    elif que[0] == s[i]:
        que.popleft()
    elif que[-1] == s[i]:
        que.pop()
    elif que[0] == s[i + 1]:
        que.append(s[i])
    elif que[-1] == s[i + 1]:
        que.appendleft(s[i])
    else:
        que.append(s[i])
print(len(que))