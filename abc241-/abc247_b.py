from collections import Counter


def main():
    cnt = Counter(sum([[*set(st)] for st in ST], []))
    for si, ti in ST:
        if 1 not in [cnt[si], cnt[ti]]:
            return print("No")
    return print("Yes")


if __name__ == '__main__':
    N = int(input())
    ST = [input().split() for _ in range(N)]

    main()
