from itertools import combinations

x = int(input())
num = [i**5 for i in range(1000)]

for a, b in combinations(num, 2):
    if a - b == x:
        print(int(a**0.2), int(b**0.2))
    elif a + b == x:
        print(int(a**0.2), -int(b**0.2))
    elif b - a == x:
        print(int(b**0.2), int(a**0.2))
    else:
        continue
    break
