a, b, n = map(int, input().split())

tmp = min(b-1, n)
print(int(a*tmp/b)-a*int(tmp/b))
