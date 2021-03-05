n, x = map(int, input().split())
a = list(map(int, input().split()))
print(*[ai for ai in a if ai != x])
