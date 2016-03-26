import MapReduce
import sys

"""
Join input from two tables
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # 0: table name
    # 1: order id
    # 2+: data
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    list_of_values.sort()
    order = list_of_values.pop(-1)
    for line_item in list_of_values:
        mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
