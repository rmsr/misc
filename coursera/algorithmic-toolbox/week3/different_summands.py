# Uses python3

def optimal_summands(n):
    summands = []
    k = n
    l = 1
    while k > 2 * l:
        summands.append(l)
        k -= l
        l += 1
    summands.append(k)
    return summands

def main(n):
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    print()

if __name__ == '__main__':
    main(int(input()))
