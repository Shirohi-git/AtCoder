def main():
    near = [0] * N
    for a, b in AB:
        near[a-1] |= (1 << b-1)
        near[b-1] |= (1 << a-1)

    dp_g = [0] * (1 << N)
    dp_g[0] = 1
    for now in range(1 << N):
        for i in range(N):
            bfo = now ^ (1 << i)
            if now >> i & 1 and dp_g[bfo]:
                dp_g[now] |= (bfo & near[i] == bfo)

    def subset(num):
        ini = num
        res = [num]
        while num > 0:
            num = (num-1) & ini
            res.append(num)
        return res

    dp_c = [1 if gi else N for gi in dp_g]
    for bit in range(1 << N):
        for sb in subset(bit >> 1 << 1):
            dp_c[bit] = min(dp_c[bit], dp_c[sb]+dp_c[bit ^ sb])
    return print(dp_c[-1])


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
