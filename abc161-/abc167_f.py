def count(t):
    r, l = 0, 0
    for ti in t:
        if ti == '(':
            l += 1
        elif ti == ')' and l >= 1:
            l -= 1
        elif ti == ')' and l < 1:
            r += 1
    return r, l


def main():
    left, right = [], []
    for si in S:
        r, l = rl = count(si)
        if r <= l:
            left.append(rl)
        elif r > l:
            right.append(rl)
    left = sorted(left)
    right = sorted(right, key= lambda x:-x[1])

    ans = 0
    for r, l in (left + right):
        if r > ans:
            ans = INF
        ans -= r - l
    return print("No" if ans else "Yes")


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    INF = 10**7

    main()
