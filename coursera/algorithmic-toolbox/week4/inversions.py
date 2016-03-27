#!/bin/python3

def merge(a, left, mid, right):
    inv = 0
    i = left
    j = mid
    b = []
    for _ in range(left, right):
        if i < mid and (j >= right or a[i] <= a[j]):
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
            # for any element i that is larger than j, i+1 thru mid are also
            # larger, so they are all inversions.
            inv += mid - i
    a[left:right] = b
    return inv

def mergesort(a, left, right):
    if right - left <= 1:
        return 0
    mid = (left + right) // 2
    inv = mergesort(a, left, mid)
    inv += mergesort(a, mid, right)
    inv += merge(a, left, mid, right)
    return inv

def main():
    input()
    a = list(map(int, input().split()))
    print(mergesort(a, 0, len(a)))

if __name__ == '__main__':
    main()
