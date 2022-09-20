import sys
sys.setrecursionlimit(10 ** 7)


def search(NUM, DESK, WHERE):
    if DESK[NUM] != -1:
        return DESK[NUM]
    else:
        if WHERE[NUM] < 0:
            return - WHERE[NUM]
        DESK[NUM] = search(WHERE[NUM], DESK, WHERE)
        return DESK[NUM]


n, q = map(int, input().split())
query = [list(map(int, input().split())) for i in range(q)]
where = ['None'] + [-i - 1 for i in range(n)]  # 下の箱 or 机の番号 #負ならば机
high = ['None'] + [i + 1 for i in range(n)]  # 箱番号 or None

for l in query:
    if where[l[2]] < 0:
        tmp = None
    else:
        tmp = where[l[2]]
    if high[l[1]] == None:
        where[l[2]] = -l[1]
    else:
        where[l[2]] = high[l[1]]
    high[l[1]] = high[l[0]]
    high[l[0]] = tmp

desk = ['None'] + [-1] * n
for i in range(1, n + 1):
    print(search(i, desk, where))
