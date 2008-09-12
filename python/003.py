def factor(x):
    factors = []
    num = x

    for i in xrange(2, int(x**0.5)):
        if num == 1:
            return factors
        while num % i == 0:
            factors.append(i)
            num = num / i
    print num
    
print factor(600851475143)[-1]