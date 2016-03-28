#!/bin/python3

"""
Compute the edit distance between two strings
"""

def main():
    print(edit_distance(input(), input()))

def edit_distance(A, B):
    a_len = len(A)
    b_len = len(B)
    # use zeroth array indexing by taking advantage of how -1 wraps to the
    # end of an array: 0-length precomputed row & column are on the 'outside'
    dist = [ [0] * b_len + [a + 1] for a in range(a_len) ]
    dist.append([ b + 1 for b in range(b_len) ] + [0])
    for i, j in [ (i, j) for i in range(a_len) for j in range(b_len) ]:
        dists = [
                dist[i][j-1] + 1,
                dist[i-1][j] + 1,
                dist[i-1][j-1] + (0 if A[i] == B[j] else 1),
            ]
        dist[i][j] = min(dists)
    return dist[-2][-2]

if __name__ == "__main__":
    main()
