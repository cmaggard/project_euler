import sys

dat = [line.split() for line in open('018.dat').readlines()][::-1]
tri = [[int(y) for y in x] for x in dat]

def compact(l_row, s_row):
  """Compacts the larger row into the smaller one, returning the smaller
     one.
     >>> compact([3,4],[7])
     [11]
     >>> compact([3,5,1],[2,4])
     [7, 9]
  """
  return [s_row[x] + max(l_row[x], l_row[x+1]) for x in xrange(len(s_row))]

if __name__ == "__main__":
  if 'test' in sys.argv:
    import doctest
    doctest.testmod()
  else:
    print reduce(compact, tri)
