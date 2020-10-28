n, s = int(input()), str(input())

# 解説AC O(N*100)ver.
num1, num2, num3 = set(), set(), set()
for i in range(n):
    num3 |= set(j + s[i] for j in num2)
    num2 |= set(j + s[i] for j in num1)
    num1.add(s[i])
print(len(num3))
