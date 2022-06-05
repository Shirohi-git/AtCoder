def main():
    half = sum(ai/bi for ai, bi in AB) / 2
    time, dist = 0, 0
    for ai, bi in AB:
        if time + ai/bi < half:
            time += ai/bi
            dist += ai
        else:
            dist += bi * (half-time)
            break
    return print(dist)


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()