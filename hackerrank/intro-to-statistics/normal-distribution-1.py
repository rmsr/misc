#! /bin/python3

import math

def ncdf(x, mean, stdev):
    return 0.5 * (1 + math.erf((x - mean) / math.sqrt(2 * stdev ** 2)))


print ncdf(40, 30, 4)
print 1 - ncdf(21, 30, 4)
print ncdf(35, 30, 4) - ncdf(30, 30, 4)
