def main():
    res = []
    que = [(A, 32)]
    while que:
        lst, num = que.pop()
        if num == -1:
            res.append(min(lst))
        elif all((li >> num & 1) for li in lst):
            nxt = [li ^ (1 << num) for li in lst]
            que.append((nxt, num-1))
        elif all((li >> num & 1) == 0 for li in lst):
            que.append((lst, num-1))
        else:
            odd = [li for li in lst if (li >> num & 1)]
            evn = [li ^ (1 << num) for li in lst if (li >> num & 1) == 0]
            que.append((odd, num-1)), que.append((evn, num-1))
    return print(min(res))


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
