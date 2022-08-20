def main():
    def imporve(lst, num):
        acc = 0
        val = [0]
        for i, ai in enumerate(lst, 1):
            acc += ai
            new = num*i - acc
            if val[-1] < new:
                new = val[-1]
            val.append(new)
        return val

    ans = a_sum = sum(A)
    x_val = imporve(A, L)
    y_val = imporve(A[::-1], R)[::-1]
    for xi, yi in zip(x_val, y_val):
        ans = min(ans, a_sum + xi+yi)
    return print(ans)


if __name__ == '__main__':
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    main()
