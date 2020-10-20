def solve(word):
    if word > 'atcoder':
        return 0
    for i, wi in enumerate(word):
        if wi != 'a':
            return i - (wi > 't')
    return -1


t = int(input())
s = [input() for _ in range(t)]
for si in s:
    print(solve(si))
