num = str(reduce(lambda x, y: x*y, xrange(1,101)))
print reduce(lambda x, y: x+y, [int(i) for i in num])
