s = input()

lst = ['', 'A']
for c in ['KIH', 'B', 'R']:
    lst = [li + c for li in lst]
    lst += [li + 'A' for li in lst]
print('YES' if s in lst else 'NO')
