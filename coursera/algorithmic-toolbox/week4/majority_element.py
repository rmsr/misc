#!/bin/python3

import random

def majority_linear(a):
    c = None
    n = 0
    for e in a:
        if not n:
            c = e
            n = 1
        else:
            n += 1 if e == c else -1
            if n == 0:
                c = None
    return c if count(a, 0, len(a) - 1, c) > len(a) // 2 else -1

def majority_recursive(a, left, right):
    if left == right:
        return a[left]
    mid = left + (right - left) // 2
    left_maj = majority_recursive(a, left, mid)
    right_maj = majority_recursive(a, mid + 1, right)
    if left_maj == right_maj:
        return left_maj
    thresh = (right - left + 1) // 2
    if left_maj > -1 and count(a, left, right, left_maj) > thresh:
        return left_maj
    if right_maj > -1 and count(a, left, right, right_maj) > thresh:
        return right_maj
    return -1

def count(a, l, r, c):
    n = 0
    for i in range(l, r+1):
        if a[i] == c:
            n += 1
    return n

def majority(a):
    return majority_linear(a)
    #return majority_recursive(a, 0, len(a) - 1)

def main():
    input()
    print(1 if majority(list(map(int, input().split()))) != -1 else 0)

if __name__ == '__main__':
    main()
