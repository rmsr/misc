
def partial_sum(i, n):
    return n * (i + n * i) // 2

def multi_sum(n):
    return partial_sum(3, n // 3) + partial_sum(5, n // 5) - partial_sum(15, n // 15)
    
[ print(multi_sum(int(input()) - 1)) for _ in range(int(input())) ]
