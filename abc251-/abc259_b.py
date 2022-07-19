from math import sin, cos


def main():
    def deg_to_rad(deg):
        from math import pi as PI
        return deg * PI / 180

    d = deg_to_rad(D)
    p = A * cos(d) - B * sin(d)
    q = A * sin(d) + B * cos(d)
    return print(p, q)


if __name__ == '__main__':
    A, B, D = map(int, input().split())

    main()
