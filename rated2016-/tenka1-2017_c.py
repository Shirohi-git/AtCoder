n = int(input())

for h in range(1, 3501):
    for w in range(h, 3501):
        bns = n * h * w
        bnb = 4 * h * w - n * (h + w)
        if bnb >= 1 and bns % bnb == 0:
            print(h, w, bns // bnb)
            exit()
