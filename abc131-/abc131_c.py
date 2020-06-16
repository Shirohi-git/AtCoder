import fractions


def lcm(x, y):  # 最小公倍数
    return (x * y) // fractions.gcd(x, y)


a, b, c, d = map(int, input().split())
all = b - (b // c + b // d - b // lcm(c, d))
part = (a - 1) - ((a - 1) // c + (a - 1) // d - (a - 1) // lcm(c, d))

print(all - part)
