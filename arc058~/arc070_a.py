x = int(input())

for t in range(x + 1):
    if t * (t + 1) >= 2 * x:
        print(t)
        break
