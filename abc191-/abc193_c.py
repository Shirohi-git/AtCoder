n = int(input())

s = set()
for i in range(2, int(n ** 0.5) + 1):
    num = i
    for _ in range(40):
        num *= i
        if num > n:
            break
        s.add(num)
print(n - len(s))
