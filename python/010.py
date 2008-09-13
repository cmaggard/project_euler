sieve = [0] * 2000000

x = 2
s = 0
while x < 2000000:
    if not sieve[x]:
        s = s + x
        n = 2 * x
        while n < 2000000:
            sieve[n] = 1
            n = x + n
    x = x + 1

print s