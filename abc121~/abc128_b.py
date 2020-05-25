n = int(input())
sp = [list(input().split()) + [i + 1] for i in range(n)]

for list in sp:
    list[1]= -int(list[1])
sp.sort()

for s, p, num in sp:
    print(num)
