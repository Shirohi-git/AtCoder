from collections import defaultdict


def main():
    parent = [0]
    val = [-1]
    note = defaultdict(lambda: 0)

    now = 0
    ans = []
    for que, num in Query:
        num = int(num)
        if que == 'ADD':
            val.append(num)
            parent.append(now)
            now = len(val) - 1
        if que == 'DELETE':
            now = parent[now]
        if que == 'SAVE':
            note[num] = now
        if que == 'LOAD':
            now = note[num]
        ans.append(val[now])
    return print(*ans)


if __name__ == '__main__':
    Q = int(input())
    Query = [(list(input().split())+[0])[:2] for _ in range(Q)]

    main()
