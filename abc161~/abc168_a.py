n = int(input()[-1])
if n == 3:
    print('bon')
elif n in set([0, 1, 6, 8]):
    print('pon')
else:
    print('hon')
