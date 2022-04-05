def main():
    stt = len(S)//2 - 1
    for le in range(stt, 0, -1):
        if S[:le] == S[le:le*2]:
            return print(le * 2)


if __name__ == '__main__':
    S = input()

    main()
