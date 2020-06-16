n, k = map(int, input().split())
d = set(range(10)) - set(map(int, input().split()))

i = n
while True:
    if (i >= n) and all(int(j) in d for j in str(i)):
        print(i)
        break
    i += 1
