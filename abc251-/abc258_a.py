def main():
    ms = (21 + K//60) % 24, K % 60
    ms = map(lambda x: str(x).zfill(2), ms)
    return print(*ms, sep=':')


if __name__ == '__main__':
    K = int(input())

    main()
