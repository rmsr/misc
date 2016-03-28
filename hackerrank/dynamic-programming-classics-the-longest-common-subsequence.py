#!/bin/python3

"""
LCS of 2 strings using table DP and backtracking to find a solution sequence

Pretty standard method.
"""

def lcs2(a, b):
    len_a = len(a)
    len_b = len(b)
    longest = [ [0] * (len_b + 1) for _ in range(len_a + 1) ]

    # compute lcs table
    for i, j in [ (i, j) for j in range(1, len_b + 1) for i in range(1, len_a + 1) ]:
        if a[i - 1] == b[j - 1]:
            longest[i][j] = longest[i-1][j-1] + 1
        else:
            longest[i][j] = max(longest[i-1][j], longest[i][j-1])

    # reconstruct sequence
    seq = []
    i = len_a
    j = len_b
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            seq.append(a[i - 1])
            i -= 1
            j -= 1
        elif longest[i - 1][j] > longest[i][j - 1]:
            i -= 1
        else:
            j -= 1
    seq.reverse()
    return seq

input()
print(*lcs2([int(i) for i in input().split()], [int(i) for i in input().split()]))
