from collections import deque

k = int(input())
lun = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(k - 1):
    tmp = lun.popleft()
    if tmp % 10 != 0:
        lun.append(tmp * 10 + (tmp % 10 - 1))
    lun.append(tmp * 10 + (tmp % 10))
    if tmp % 10 != 9:
        lun.append(tmp * 10 + (tmp % 10 + 1))

print(lun.popleft())
