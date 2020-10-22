def printrow(num, s, t):
    for i in range(50):
        for j in range(100):
            res = ((i + j) % 3 == 0) & ((num - 1) * i > 0)
            print(s if res else t, end='')
            num -= res
        print()

a, b = map(int, input().split())

print(100, 100)
printrow(b, '#', '.')
printrow(a, '.', '#')
