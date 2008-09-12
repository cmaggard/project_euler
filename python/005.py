def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

result = 1
for i in range(2,21):
    result = lcm(result, i)

print result