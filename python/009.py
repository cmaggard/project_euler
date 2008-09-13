def fun():
    for a in xrange(1,999):
        for b in xrange(a+1,1000-a):
            c = 1000 - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                print a * b * c
                return

fun()