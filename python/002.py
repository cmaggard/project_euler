def fib():
    a, b = 1, 1
    while b < 4000000:
        yield b
        a, b = b, a + b
        
print sum(filter(lambda x: x % 2 == 0, fib()))