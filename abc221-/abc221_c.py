def main():
    l = len(N)
    ans = 0
    for bit in range(1 << l):
        a, b = ['0'], ['0']
        for i in range(l):
            a.append(N[i])
            if (bit >> i) & 1:
                b.append(a.pop())
        num = int(''.join(a)) * int(''.join(b))
        ans = max(ans, num)
    return print(ans)


if __name__ == '__main__':
    N = sorted(input())[::-1]

    main()
