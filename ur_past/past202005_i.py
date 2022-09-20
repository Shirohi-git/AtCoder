from numpy import matrix

n = int(input())
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
row = matrix([i for i in range(n)])
col = matrix([j for j in range(n)])

t = 1
for q in query:
    if q[0] == 1:
        row[:,[q[1] - 1, q[2] - 1]] = row[:,[q[2] - 1, q[1] - 1]]
    if q[0] == 2:
        col[:,[q[1] - 1, q[2] - 1]] = col[:,[q[2] - 1, q[1] - 1]]
    if q[0] == 3:
        tmp = row[:]
        row = col[:]
        col = tmp[:]
        t *= -1
    if q[0] == 4:
        if t == 1:
            print(n * row[0, q[1] - 1] + col[0, q[2] - 1])
        if t == -1:
            print(n * col[0, q[2] - 1] + row[0, q[1] - 1])
