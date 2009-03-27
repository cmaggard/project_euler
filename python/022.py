import sys

a = ord('A') - 1
def alpha_val(name):
  """
  >>> alpha_val("COLIN")
  53
  """
  return sum([ord(x) - a for x in name])

if __name__ == "__main__":
  if 'test' in sys.argv:
    import doctest
    doctest.testmod()
  else:
    data = [x[1:len(x)-1] for x in open('022.dat').readline().split(",")]
    data.sort()
    print sum([alpha_val(data[x] * (x + 1)) for x in xrange(len(data))])
