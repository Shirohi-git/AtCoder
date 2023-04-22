from math import gcd


def main():
    # g:ループの数 l:ループの長さ
    g = gcd(D, N)
    if g == 1:
        ans = (D*(K-1)) % N
    else:
        g_id, l_id = divmod(K-1, N//g)
        ans = (g_id + D*l_id) % N
    return print(ans)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, D, K = map(int, input().split())

        main()
