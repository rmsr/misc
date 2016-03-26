# Uses python3
import sys
from collections import namedtuple

Item = namedtuple('Item', 'value weight')

def get_optimal_value(capacity, items):
    total = 0.

    for item in sorted(items, key=lambda i: i.value / i.weight, reverse=True):
        if item.weight <= capacity:
            total += item.value
            capacity -= item.weight
        elif capacity:
            total += item.value * capacity / item.weight
            capacity = 0
        if not capacity:
            break

    return total

def main(entries):
    n, capacity = map(int, entries[0])
    items = [ Item(*map(int, e)) for e in entries[1:] ]
    opt_value = get_optimal_value(capacity, items)
    print("{:.10f}".format(opt_value))

if __name__ == "__main__":
    main([l.split() for l in sys.stdin.readlines()])
