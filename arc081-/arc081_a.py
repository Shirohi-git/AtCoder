from collections import Counter

n = int(input())
a = list(map(int, input().split()))

acnt = Counter(a)
num = [0,0]
for i in acnt:
    if acnt[i] >= 4:
        num.append(i)
    if acnt[i] >= 2:
        num.append(i)
num.sort()
print(num[-1] * num[-2])
