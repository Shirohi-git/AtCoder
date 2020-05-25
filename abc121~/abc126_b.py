s = str(input())
a, b = int(s[:2]), int(s[2:])

if 1 <= a <= 12:
    print('AMBIGUOUS' if 1 <= b <= 12 else 'MMYY')
else:
    print('YYMM' if 1 <= b <= 12 else 'NA')
