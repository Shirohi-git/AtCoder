def main():
    v = V
    for i in range(V+1):
        v -= ABC[i % 3]
        if v < 0:
            idx = i % 3
            break
    return print('FMT'[idx])


if __name__ == '__main__':
    V, *ABC = map(int, input().split())

    main()
