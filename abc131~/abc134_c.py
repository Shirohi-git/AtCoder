n = int(input())
a = [int(input()) for i in range(n)]
a_1 = max(a)
a_2 = sorted(a)[-2]
for i in a:
    if i != a_1:
        print(a_1)
    else:
        print(a_2)
