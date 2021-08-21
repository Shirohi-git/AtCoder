def main():
    last = [0] * 26
    acc = [0, 1, 1]
    for i, si in enumerate(S, 1):
        idx = ord(si) - ord_a
        acc += [acc[-1] + acc[-2] - acc[last[idx]]]
        acc[-1] %= MOD1
        last[idx] = i
    return print(acc[-1]-1)


if __name__ == '__main__':
    S = input()
    ord_a = ord('a')
    MOD1 = 10**9 + 7

    main()
