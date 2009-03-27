import math

def fib():
  a, b = 1, 1
  while True:
    yield a
    a, b = b, a + b

gen = fib()
term = 1
while True:
  x = gen.next()
  if math.log10(x) >= 999:
    print term
    exit()
  term += 1
