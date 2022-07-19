def main():
    if S[0] != T[0]:
        return print("No")

    s, nxt = [S[0]], 1
    for i, ti in enumerate(T[1:], 1):
        if T[i:i+2] != S[nxt:nxt+2] and s[-1] == S[nxt]:
            s.append(ti)
        elif ti == S[nxt]:
            s.append(S[nxt])
            nxt += 1
    return print('Yes' if ''.join(s) == T else 'No')


if __name__ == '__main__':
    S, T = input(), input()

    main()
