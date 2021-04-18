a, b = map(int, input().split())

for i in range(b, 0, -1):
    if (a + i - 1) // i < b // i:
        exit(print(i))
