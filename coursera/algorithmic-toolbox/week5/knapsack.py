#!/bin/python3

"""
Knapsack without repetitions, for items with 1:1 weight:value ratio

What optimizations are available for value equivalent to weight?
"""

def main():
    maximum = int(input().split()[0])
    weights = [ int(i) for i in input().split() ]
    print(optimal_weight_matrix(maximum, weights))


def optimal_weight_matrix(maximum, weights):
    values = [ [0] * (len(weights) + 1) for _ in range(maximum + 1) ]
    for item in range(1, len(weights) + 1):
        for subweight in range(1, maximum + 1):
            values[subweight][item] = values[subweight][item - 1]
            weight = weights[item - 1]
            if weight <= subweight:
                value = values[subweight - weight][item - 1] + weight
                values[subweight][item] = max(value, values[subweight][item])
    return values[-1][-1]


def optimal_weight_defaultdict(maximum, weights):
    """
    Instead of a values matrix, use a defaultdict. TOO MUCH MEMORY!
    """
    from collections import defaultdict
    values = defaultdict(int)

    for item in range(len(weights)):
        for subweight in range(1, maximum + 1):
            values[subweight, item] = values[subweight, item - 1]
            weight = weights[item]
            if weight <= subweight:
                value = values[subweight - weight, item - 1] + weight
                values[subweight, item] = max(value, values[subweight, item])
    return values[maximum, len(weights) - 1]


if __name__ == '__main__':
    main()
