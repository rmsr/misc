#!/bin/python3
import random

def partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    k = j + 1
    for i in range(j + 1, r + 1):
        if a[i] == x:
            a[i], a[k] = a[k], a[i]
            k += 1
    return j, k

def quicksort(a, l, r):
    if l >= r:
        return
    p = random.randint(l, r)
    a[l], a[p] = a[p], a[l]
    j, k = partition(a, l, r)
    quicksort(a, l, j - 1);
    quicksort(a, k, r);

def main():
    input()
    a = list(map(int, input().split()))
    quicksort(a, 0, len(a) - 1)
    print(*a)

if __name__ == '__main__':
    main()
