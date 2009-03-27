def sum_facts(num):
  """
  >>> facts(220)
  284
  >>> facts(284)
  220
  """
  return sum([x for x in xrange(1,num/2+1) if not num % x])

total = 0
used = set()
for x in xrange(1,10000):
  y = sum_facts(x)
  if sum_facts(y) == x and y != x and x not in used and y not in used:
    used.add(x)
    used.add(y)
    total += x + y

print total

