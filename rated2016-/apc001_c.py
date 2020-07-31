def mfvinput(i):
    print(i)
    seat[i] = input()
    if seat[i] == 'Vacant':
        exit()

n = int(input())
seat = [None] * n

mfvinput(0), mfvinput(n - 1)
l, r = 0, n
for _ in range(20):
    tmp = (l + r) // 2
    mfvinput(tmp)
    if (tmp % 2 == l % 2) == (seat[tmp] == seat[l]):
        l = tmp
    else:
        r = tmp
