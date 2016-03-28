#!/bin/python3

"""
Primitive calculator

Given ops *3, *2, +1, what is the fewest ops to reach n from 1?
"""

import os
import sys

def main():
    sequence = optimal_sequence_linear(int(input()))
    print(len(sequence) - 1)
    print(*sequence)

def optimal_sequence_linear(n):
    """
    Solve by calculating min-steps for each i in 1..n
    """
    steps = [0] * (n + 1)

    # calculate array
    for i in range(1, n + 1):
        prev = [ steps[i - 1] ]
        if not i % 3:
            prev.append(steps[i // 3])
        if not i % 2:
            prev.append(steps[i // 2])
        steps[i] = min(prev) + 1
    # now work backwards to find the solution
    seq = []
    while n:
        seq.append(n)
        prev = [ (steps[n-1], n-1) ]
        if not n % 3:
            prev.append((steps[n // 3], n // 3))
        if not n % 2:
            prev.append((steps[n // 2], n // 2))
        prev.sort()
        n = prev[0][1]
    seq.reverse()
    return seq

class SolutionFound(Exception): pass

def optimal_sequence_bfs_nested(n):
    """
    Solving this as BFS of a math ops DAG, each vertex with 3 edges. Whichever
    branch gets n to 1 first is the keeper. TOO SLOW.
    """
    if n == 1:
        return [1]

    ops = [
            lambda n: 0 if n % 3 else n // 3,
            lambda n: 0 if n % 2 else n // 2,
            lambda n: n - 1
        ]

    solution = None
    queue = [ (n,) ]
    try:
        while True:
            previous = queue
            queue = []
            for steps in previous:
                for new in [ op(steps[0]) for op in ops ]:
                    if new == 1:
                        solution = steps
                        raise SolutionFound
                    if new > 1:
                        queue.append((new, steps))
    except SolutionFound:
        pass
    sequence = [1]
    try:
        while True:
            sequence.append(solution[0])
            solution = solution[1]
    except IndexError:
        pass
    return sequence
 
if __name__ == "__main__":
    main()
