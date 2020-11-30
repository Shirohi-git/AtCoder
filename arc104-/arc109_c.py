n, k = map(int, input().split())
s = list(input()[::-1]) * 2

ptn, win = 'PRPP_RSRR_SPSS', 'PRS'
for _ in range(k):
    tmp = []
    while s:
        hand = ptn.index(s.pop() + s.pop())
        tmp.append(win[hand // 5])
    s = tmp[::-1] * 2
print(s.pop())
