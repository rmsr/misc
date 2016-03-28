#!/bin/python3

"""
Compute 3-way longest common subsequence
"""

def main():
    _, a = input(), [ int(i) for i in input().split() ]
    _, b = input(), [ int(i) for i in input().split() ]
    _, c = input(), [ int(i) for i in input().split() ]
    print(lcs3(a, b, c))


def lcs3(a, b, c):
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    longest = [ [ [0] * (len_c + 1) for _ in range(len_b + 1) ] for _ in
            range(len_a + 1) ]
    
    # compute lcs table
    for i, j, k in [ (i, j, k) for k in range(1, len_c+1) for j in range(1, len_b+1) for i in range(1, len_a+1) ]:
        if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
            longest[i][j][k] = longest[i-1][j-1][k-1] + 1
        else:
            longest[i][j][k] = max(longest[i-1][j][k], longest[i][j-1][k], longest[i][j][k-1])
    return longest[-1][-1][-1]


if __name__ == '__main__':
    main()
