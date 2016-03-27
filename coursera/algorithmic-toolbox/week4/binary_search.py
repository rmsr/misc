#! /bin/python3

def binary_search(a, x):
    left, right = 0, len(a)
    while True:
        if left == right:
            return -1
        mid = left + (right - left) // 2
        if x < a[mid]:
            right = min(mid, right - 1)
            continue
        if x > a[mid]:
            left = max(mid, left + 1)
            continue
        return mid

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def main():
    _, *a = map(int, input().split()) # already sorted
    _, *b = map(int, input().split())
    print(binary_search(a, x) for x in b)

if __name__ == '__main__':
    main()
