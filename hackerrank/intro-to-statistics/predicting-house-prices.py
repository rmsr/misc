#!/bin/python3

"""
Multiple-feature closed-form linear regression in pure python

This is unlikely to be fast on nontrivial datasets. Still pretty cool though.
"""

def invert(A):   
    # filched from http://www.alphasheep.co.za/2015/06/on-matrix-inversion-in-python.html
    A = [A[i]+[int(i==j) for j in range(len(A))] for i in range(len(A))]    
    for i in range(len(A)):
        A[i:] = sorted(A[i:], key=lambda r: -abs(r[i]))
        A[i] = [A[i][j]/A[i][i] for j in range(len(A)*2)]
        A = [[A[j][k] if i==j else A[j][k]-A[i][k]*A[j][i] for k in range(len(A)*2)] for j in range(len(A))]
    return [A[i][-len(A):] for i in range(len(A))]

def matmult(M, N):
    return [[sum(a*b for a,b in zip(rowM, colN)) 
             for colN in zip(*N)] for rowM in M]

# (X-transpose * X)-inverted * X-transpose * Y
def regress(features, output):
    transposed = list(zip(*features))
    W = matmult(matmult(invert(matmult(transposed, features)), transposed), output)
    return [ r[0] for r in W ]

def predict(model, features):
    return sum(a*b for a, b in zip(model, [1] + features))

def main():
    D, N = map(int, input().split())
    data = [ [ float(f) for f in input().split() ] for _ in range(N) ]
    features = [ [1] + row[:-1] for row in data ]
    output = [ [ row[-1] ] for row in data ]
    model = regress(features, output)
    for _ in range(int(input())):
        print(predict(model, [ float(f) for f in input().split() ] ))

main()
