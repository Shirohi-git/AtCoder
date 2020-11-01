n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
print(sum(vi - ci for vi, ci in zip(v, c) if vi >= ci))
