import MapReduce
import sys

"""
Find all asymmetric friendships

Find all (friend, person)/(person, friend) such that (person, friend) and not
(friend, person). Yes, tuples of both directions must be returned for the
grader to pass this.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person, friend = record
    mr.emit_intermediate(person, ('friend', friend))
    mr.emit_intermediate(friend, ('person', person))

def reducer(key, list_of_values):
    persons = [ v[1] for v in list_of_values if v[0] == 'person' ]
    friends = [ v[1] for v in list_of_values if v[0] == 'friend' ]
    difference = list(set(persons).symmetric_difference(set(friends)))
    for p in difference:
        mr.emit((key, p))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
