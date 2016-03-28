#!/bin/python3

"""
Place parentheses in a list of integers and math ops to maximize value

Ops are add, sub, mult
"""

import operator
import re

ops_table = { '+': operator.add, '-': operator.sub, '*': operator.mul }

def main():
    expression = input()
    data = [ int(i) for i in re.findall('\d+', expression) ]
    ops = [ ops_table[c] for c in re.findall('[+*-]', expression) ]
    print(get_maximum_value(data, ops))

def get_maximum_value(data, ops):
    min_vals = make_array(data)
    max_vals = make_array(data)

    for s in range(1, len(data)):
        for i, j in [ (n, s + n) for n in range(len(data) - s) ]:
            vals = []
            for k in range(i, j):
                op = ops[k]
                vals.extend([
                        op(max_vals[i][k], max_vals[k+1][j]),
                        op(min_vals[i][k], max_vals[k+1][j]),
                        op(max_vals[i][k], min_vals[k+1][j]),
                        op(min_vals[i][k], min_vals[k+1][j]),
                    ])
            min_vals[i][j] = min(vals)
            max_vals[i][j] = max(vals)
    return max_vals[0][-1]

def make_array(data):
    n = len(data)
    array = [ [0] * n for _ in range(n) ]
    for i in range(n):
        array[i][i] = data[i]
    return array

if __name__ == "__main__":
    main()
