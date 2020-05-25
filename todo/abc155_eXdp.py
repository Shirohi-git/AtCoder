N = input()
m = [0]+list(N)
n = [int(m[i]) for i in range(len(m))]

for i in range(len(n)):
    if n[(i + 1) * (-1)] >= 10:
        n[(i + 1) * (-1)] -= 10
        n[(i + 2) * (-1)] += 1
    elif n[(i + 1) * (-1)] >= 6:
        n[(i + 2) * (-1)] += 1
        n[(i + 1) * (-1)] = 0
    elif n[(i + 1) * (-1)] == 5:
        if n[(i + 2) * (-1)] >= 5:
            n[(i + 2) * (-1)] += 1
            n[(i + 1) * (-1)] = 0
cnt = sum(n)

num = 0
ten = 1
for i in n[::-1]:
    num += i * ten
    ten *= 10

m = num - int(N)
n = [0] + list(str(m))
n = [int(n[i]) for i in range(len(n))]
cnt += sum(n)

print(cnt)
