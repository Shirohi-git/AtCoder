def main():
    path = "./score.txt"
    with open(path) as f:
        lst = [fi for fi in f.readlines()][2::4]
    lst = list(map(lambda x: int(x.split()[2]), lst))
    res = sum(lst)
    print(res)

    for i in range(len(lst)):
        lst[i] = str(i).zfill(4)+' ; '+str(lst[i])
    lst.append('sum  ; '+str(res))
    with open(path, 'w') as f:
        f.write('\n'.join(lst))
    return


if __name__ == "__main__":
    main()
