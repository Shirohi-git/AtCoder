def main():
    from collections import Counter
    from itertools import permutations

    def write_index(char, lst):
        rev = lst[::-1]
        idx_cnt = [idx[ri] for ri in rev]
        for i, si in enumerate(S):
            if si != char:
                continue
            while idx_cnt[-1] == 0:
                idx_cnt.pop()
            ans[i] = rev[len(idx_cnt)-1] + 1
            idx_cnt[-1] -= 1
        return

    idx = [0] * 6
    cnt = list(map(Counter, (S[:N], S[N:2*N], S[2*N:])))
    for i, abc in enumerate(permutations(range(3))):
        c = min(cnt[p][q] for p, q in zip(abc, ABC))
        for p, q in zip(abc, ABC):
            cnt[p][q] -= c
        idx[i] += c

    ans = [0] * (3 * N)
    write_index('A', [0, 1, 2, 3, 4, 5])
    write_index('B', [2, 4, 0, 5, 1, 3])
    write_index('C', [3, 5, 1, 4, 0, 2])
    # ["ABC", "ACB", "BAC", "CAB", "BCA", "CBA"]
    return print(*ans, sep='')


if __name__ == '__main__':
    N, S = int(input()), input()
    ABC = "ABC"

    main()
