x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ab = sorted(ai + bj for ai in a for bj in b)[-k:]
abc = sorted(abi + cj for abi in ab for cj in c)[-k:]
print(*abc[::-1], sep='\n')
