from math import sin, cos, atan2, degrees, pi as PI


def main():
    for ei in e:
        px = 0
        theta = 2 * PI * (ei % t)/t
        py = -l * cos(theta - PI/2) / 2
        pz = l * sin(theta - PI/2) / 2 + l/2

        dist = ((x-px)**2 + (y-py)**2)**0.5
        ans = degrees(atan2(pz, dist))
        print(ans)


if __name__ == '__main__':
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    e = [int(input()) for _ in range(q)]
    main()
