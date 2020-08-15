s = input()

for i in [3, 2, 1, 0]:
    if 'R' * i in s:
        print(i)
        break
