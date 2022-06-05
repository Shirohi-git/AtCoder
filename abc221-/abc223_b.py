def main():
    sl = len(S)
    sft = []
    for i in range(sl):
        s = ''.join([S[(j+i) % sl] for j in range(sl)])
        sft.append(s)
    sft = sorted(sft)
    return print(sft[0], sft[-1], sep='\n')


if __name__ == '__main__':
    S = input()

    main()