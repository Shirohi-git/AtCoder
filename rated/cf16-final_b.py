n = int(input())

for i in range(1,3 * int(n ** 0.5)):
    n -= i
    if n < i + 1:
        maximum = i + 1
        no = i + 1 - n
        break

for i in range(maximum):
    if i + 1 == no:
        continue
    print(i + 1)
