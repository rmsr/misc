#!/bin/python3

import math

def pcls(max, n, mean, stdev):
    z = (max / n - mean) * math.sqrt(n) / stdev
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))
    
max = 9800
n = 49
mean = 205
stdev = 15

print(pcls(max, n, mean, stdev))
