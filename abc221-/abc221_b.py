def main():
    new = S
    for i in range(len(S)):
        if S[i] != T[i]:
            new = S[:i] + S[i+1] + S[i] + S[i+2:]
            break
    return print('Yes' if new == T else 'No')


if __name__ == '__main__':
    S, T = input()+'_', input()+'_'

    main()
