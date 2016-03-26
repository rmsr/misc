# Uses python3

# this is almost offensively simple
def main(n):
    r = n // 10
    n %= 10
    return r + n // 5 + n % 5

if __name__ == '__main__':
    print(main(int(input())))
