import MapReduce
import sys

"""
Friend count
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person, friend = record
    mr.emit_intermediate(person, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, sum(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
