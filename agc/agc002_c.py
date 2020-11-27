n, l = map(int, input().split())
a = list(map(int, input().split()))

link = [a[i] + a[i + 1] for i in range(n - 1)]
idx = link.index(max(link))

res = ['Impossible']
if link[idx] >= l:
    res = ['Possible'] + [i + 1 for i in range(idx)]
    res += [i for i in range(n - 1, idx + 1, -1)] + [idx + 1]
print(*res, sep='\n')
