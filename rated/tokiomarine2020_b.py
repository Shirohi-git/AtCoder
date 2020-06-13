a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a > b:
    a -= v * t
    b -= w * t
    print('YES' if a <= b else 'NO')
elif a < b:
    a += v * t
    b += w * t
    print('YES' if a >= b else 'NO')

