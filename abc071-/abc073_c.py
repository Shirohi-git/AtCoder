n = int(input())
a = [int(input()) for _ in range(n)]

cnt = set([])
for i in a:
    if i in cnt:
        cnt.discard(i)
    else:
        cnt.add(i)
print(len(cnt))
