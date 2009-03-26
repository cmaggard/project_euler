def triangle():
  n, s = 3, 3
  while True:
    yield s
    s, n = s + n, n + 1

def divisors(number):
  n = number
  factors = {}
  while n != 1:
    x = 2
    while n % x:
      x += 1
    n /= x
    try:
      factors[x] += 1
    except KeyError:
      factors[x] = 1
  fac_count = [factors[x] + 1 for x in factors.keys()]
  return reduce(lambda x, y: x * y, fac_count)

tri_gen = triangle()
largest = (0, 0)
while largest[0] <= 500:
  n = tri_gen.next()
  res = divisors(n)
  if res > largest[0]:
    largest = (res, n)

print largest[1]
