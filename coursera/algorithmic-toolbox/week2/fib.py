# Uses python3
def fib(n):
    if n < 2:
        return n
    prev = 1
    cur = 1
    for i in range(2, n):
        prev, cur = cur, prev + cur
    return cur

n = int(input())
print(fib(n))
