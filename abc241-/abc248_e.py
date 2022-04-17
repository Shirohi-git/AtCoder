from math import gcd


def gcd3(x, y, z):
    if x < 0 or (x == 0 and y < 0):
        x, y, z = -x, -y, -z
    t = gcd(x, gcd(y, z))
    return x//t, y//t, z//t


def main():
    if K == 1:
        return print('Infinity')

    ans = set()
    for i in range(N):
        s, t = XY[i]
        for j in range(i+1, N):
            u, v = XY[j]
            cnt = 0
            for x, y in XY:
                cnt += ((t-v)*(x-s) == (y-t)*(s-u))
            if cnt >= K:
                ans.add(gcd3(v-t, s-u, s*(t-v) - t*(s-u)))
    return print(len(ans))


if __name__ == '__main__':
    N, K = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
