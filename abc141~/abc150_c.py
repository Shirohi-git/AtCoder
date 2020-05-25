import itertools as it

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

cnt = 0
for i in it.permutations([i for i in range(1, n + 1)], n):
    cnt += 1
    if list(i) == p:
        a = cnt
    if list(i) == q:
        b = cnt
        
print(abs(a-b))