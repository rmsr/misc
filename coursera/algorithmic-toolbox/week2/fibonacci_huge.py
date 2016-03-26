# Uses python3
import sys

def get_fibonaccihuge_pisano(n, m):
    sequence = []
    prev = 0
    cur = 1
    median = 0
    while sequence[:median] != sequence[median:] or not median:
        sequence.append(prev % m)
        median = len(sequence) // 2
        prev, cur = cur, prev + cur
    return sequence[n % median]


def matrix_mod_mult_2x2(a, b, m):
    a1, a2, a3, a4 = a[0] + a[1]
    b1, b2, b3, b4 = b[0] + b[1]
    return (((a1*b1 + a2*b3) % m,
             (a1*b2 + a2*b4) % m   ),
            ((a3*b1 + a4*b3) % m,
             (a3*b2 + a4*b4) % m   ))

def matrix_pow_mod(M, p, m):
    if p == 1:
        return M
    R = matrix_pow_mod(M, p//2, m)
    R = matrix_mod_mult_2x2(R, R, m)
    if p % 2:
        R = matrix_mod_mult_2x2(M, R, m)
    return R

def get_fibonaccihuge_matrix(n, m):
    start = ((1, 1), (1, 0))
    # top left is fib(n+1)
    return matrix_pow_mod(start, n-1, m)[0][0]

def main():
    n, m = map(int, input().split())
    print(get_fibonaccihuge_matrix(n, m))

if __name__ == '__main__':
    main()
