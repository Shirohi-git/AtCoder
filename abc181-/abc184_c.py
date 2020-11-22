r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

ar, ac = abs(r1 - r2), abs(c1 - c2)
p1, p2 = r1 + c1, r2 + c2
m1, m2 = r1 - c1, r2 - c2

if (r1, c1) == (r2, c2):
    print(0)
elif m1 == m2 or p1 == p2 or ar + ac <= 3:
    print(1)
elif (p1 % 2 == p2 % 2 or ar + ac <= 6
      or abs(p1 - p2) <= 3 or abs(m1 - m2) <= 3):
    print(2)
else:
    print(3)
