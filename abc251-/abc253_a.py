def main():
    _, b, _ = ABC
    return print('Yes' if b == sorted(ABC)[1] else 'No')


if __name__ == '__main__':
    ABC = list(map(int, input().split()))

    main()
