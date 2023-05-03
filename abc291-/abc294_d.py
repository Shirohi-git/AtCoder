from heapq import heappop, heappush


def main():
    call = 1
    notcome = 1
    came = [N+1]
    for t, x in Event:
        if t == 1:
            call += 1
        elif t == 2:
            heappush(came, x)
        elif t == 3:
            while notcome == came[0]:
                heappop(came)
                notcome += 1
            print(notcome)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    Event = [list(map(int, input().split())) for _ in range(Q)]
    Event = [(ei + [0])[:2] for ei in Event]

    main()
