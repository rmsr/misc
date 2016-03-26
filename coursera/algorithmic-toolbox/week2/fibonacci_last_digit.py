# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n < 2:
        return n
    prev = 1
    cur = 1
    for i in range(2, n):
        prev, cur = cur, prev + cur % 10
    return cur % 10


if __name__ == '__main__':
    print(get_fibonacci_last_digit(int(input())))
