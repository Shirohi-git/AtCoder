n = int(input())
a = list(map(int, input().split()))

cnt2 = sum(i % 4 == 2 for i in a)
cnt4 = sum(i % 4 == 0 for i in a)
print('Yes 'if n <= 2 * cnt4 + max(1, cnt2) else 'No')
