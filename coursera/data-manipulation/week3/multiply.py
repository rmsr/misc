import MapReduce
import sys

"""
matrix multiplication
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# A = L x M
# B = M x N

L = N = M = 5

def mapper(record):
    # key: matrix name
    # value: i, j, value
    name, i, j, value = record
    if name == 'a':
        for k in range(N):
            mr.emit_intermediate((i, k),('a', i, j, value))
    else:
        for k in range(L):
            mr.emit_intermediate((k, j),('b', i, j, value))

def reducer(key, vals):
    # key: i, j
    # value: list of matrix cells
    i, j = key
    a = { (i, j): value for name, i, j, value in vals if name == 'a' }
    b = { (i, j): value for name, i, j, value in vals if name == 'b' }
    tot = sum( a[i, k] * b[k, j] for k in range(M) if (i, k) in a and (k, j) in b )
    mr.emit((i, j, tot))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
