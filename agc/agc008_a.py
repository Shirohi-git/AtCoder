x, y = map(int, input().split())

if x <= y:
    print(min(abs(y - x), abs(y + x) + 1))
elif x > y:
    print(min(abs(y - x) + 2, abs(y + x) + 1))
