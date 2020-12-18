n = int(input())
a, b = map(int, input().split())

if n <= a or a > b or (a == b and n % (a + 1) > 0):
    print('Takahashi')
elif b > a or (a == b and n % (a + 1) == 0):
    print('Aoki')
