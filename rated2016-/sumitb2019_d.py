n, s = int(input()), str(input())

num1, num2, num3 = set([]), set([]), set([])
for i in range(n):
    if s[i] in num1:
        continue
    num1.add(s[i])
    for j in range(i + 1, n):
        tmp2 = s[i] + s[j]
        if tmp2 in num2:
            continue
        num2.add(tmp2)
        for k in range(j + 1, n):
            num3.add(tmp2 + s[k])
print(len(num3))
