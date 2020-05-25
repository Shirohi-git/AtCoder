from itertools import combinations


def dist(i, j):
    return ((i[0]-j[0])**2+(i[1]-j[1])**2)**0.5


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
l = combinations([i for i in range(n)], 2)
length = [dist(xy[i], xy[j]) for i, j in l]

print(2*sum(length)/n)
