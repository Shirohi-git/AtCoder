def main():
    pin = [0] * 7
    for i, si in enumerate(S):
        pin[D[i]] += int(si)

    res = 0
    for i in range(7):
        for j in range(i-1):
            if pin[i] > 0 and pin[j] > 0:
                res |= all(pin[k] == 0 for k in range(j+1, i))

    if S[0] == '1':
        res = 0
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    S = input()
    D = {6: 0, 3: 1, 1: 2, 7: 2, 0: 3, 4: 3, 2: 4, 8: 4, 5: 5, 9: 6}

    main()
