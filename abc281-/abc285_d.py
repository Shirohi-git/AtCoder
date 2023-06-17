from collections import defaultdict


def topological(N, edge0):
    from collections import deque

    incnt = defaultdict(lambda: 0)
    child = defaultdict(set)
    for a, b in edge0:
        child[b].add(a)
        incnt[a] += 1
        incnt[b] += 0

    tprg = []
    que = deque([i for i, num in incnt.items() if num == 0])
    while que:
        q = que.popleft()
        for i in child[q]:
            incnt[i] -= 1
            if incnt[i] == 0:
                que.append(i)
        tprg.append(q)
    
    return sum(incnt.values()) == 0 


def main():
    res = topological(N, AB)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N = int(input())
    AB = [input().split() for _ in range(N)]

    main()
