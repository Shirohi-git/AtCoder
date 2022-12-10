def main():
    if len(S) != 8:
        return print('No')

    a, *num, z = S
    res = True
    if not((a in ALP_s) and (z in ALP_s) and len(num) == 6):
        res &= False
    try:
        num = int(''.join(num))
        res &= (10**5 <= num < 10**6)
    except:
        res &= False
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    S = input()
    ALP_s = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    main()
