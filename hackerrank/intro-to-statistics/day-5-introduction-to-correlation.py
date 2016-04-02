#!/bin/python3

import math
import statistics

popularity = [10., 9.8, 8., 7.8, 7.7, 7., 6., 5., 4., 2.]  
price = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

def pearson(A, B):
    M = len(A)
    assert M == len(B)
    A_mean = statistics.mean(A)
    A_stdev = statistics.pstdev(A)
    B_mean = statistics.mean(B)
    B_stdev = statistics.pstdev(B)
    cross_mean = sum(A[i] * B[i] for i in range(M)) / M
    return (cross_mean - A_mean * B_mean) / (A_stdev * B_stdev)

def rank(A):
    return [ r for r, v in sorted(enumerate(sorted(enumerate(A), key=lambda e: e[1])), key=lambda e: e[1][0]) ]

def spearman(A, B):
    M = len(A)
    assert M == len(B)
    A_rank = rank(A)
    B_rank = rank(B)
    return 1 - (6 * sum((A_rank[i] - B_rank[i])**2 for i in range(M)) / (M * (M**2 - 1)))
    
print("{:.3f}\n{:.1f}".format(pearson(popularity, price), spearman(popularity, price)))
