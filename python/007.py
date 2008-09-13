primes = [2, 3, 5, 7, 11, 13]

x = 14

def isprime(x):
    for n in primes:
        if x % n == 0:
            return False
    return True

while len(primes) != 10001:
    if isprime(x):
        primes.append(x)
    x = x + 1

print primes[10000]