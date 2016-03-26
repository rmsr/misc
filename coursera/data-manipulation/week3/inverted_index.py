import MapReduce
import sys

"""
Create inverted index from documents
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    docid, text = record
    for w in text.split():
      mr.emit_intermediate(w, docid)

def reducer(key, list_of_values):
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
