from collections import Counter


def main():
    rote = []
    for i, pi in enumerate(P):
        rote += [i-pi, i-pi-1, i-pi+1]
    rote = [ri % N for ri in rote]
    cnt = Counter(rote)
    return print(max(cnt.values()))


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    main()
