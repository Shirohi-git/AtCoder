def main():
    ans = []
    ids = [i for i in range(63) if X >> i & 1]
    for i in range(1 << len(ids)):
        num = 0
        for j, idx in enumerate(ids):
            if (i >> j) & 1:
                num += (1 << idx)
        ans.append(num)

    for ai in ans:
        print(ai)
    return


if __name__ == '__main__':
    X = int(input())

    main()
