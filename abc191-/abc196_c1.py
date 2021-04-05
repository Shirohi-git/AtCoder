n = int(input())

for i in range(10 ** 6 + 1):
    if int(str(i) * 2) > n:
        exit(print(i - 1))
