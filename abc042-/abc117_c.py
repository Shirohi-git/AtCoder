n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

if n >= m:
    print(0)
else:
    x = sorted([x[i] - x[i - 1] for i in range(1, m)])
    print(sum(x[:m-n]))
