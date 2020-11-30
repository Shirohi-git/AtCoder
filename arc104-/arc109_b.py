n = int(input())

x = int((8 * n + 9)** 0.5 // 2)
while x * (x + 1) > 2 * (n + 1):
    x -= 1
print(n + 1 - x)
