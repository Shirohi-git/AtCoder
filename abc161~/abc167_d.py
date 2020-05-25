import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt, town = 0, 1
l, s = [], set()
while True:
    town = a[town - 1]
    cnt += 1
    if cnt == k:
        print(town)
        exit()
    if town in s:
        loop_start = town
        break
    l.append(town)
    s.add(town)

loop_cnt = l.index(loop_start)
loop = l[loop_cnt:]
print(loop[(k - loop_cnt) % len(loop) - 1])
