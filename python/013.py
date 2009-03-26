lines = open("013.dat").readlines()

res = reduce(lambda x, y: x+y, [int(line) for line in lines])

print str(res)[:10]

