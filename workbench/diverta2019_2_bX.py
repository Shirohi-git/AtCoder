from collections import defaultdict
from itertools import product

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

cnt = defaultdict(int)
