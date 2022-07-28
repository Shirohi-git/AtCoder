from collections import Counter


def main():
    for k, v in Counter(S).items():
        if v == 1:
            return print(k)
    return print(-1)


if __name__ == '__main__':
    S = input()

    main()
