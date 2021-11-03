def main():
    from itertools import permutations

    ans = set()
    for itr in permutations(S):
        ans.add(''.join(itr))
    return print(len(ans))


if __name__ == '__main__':
    S = input()

    main()
