def palindrome(x):
    s = str(x)
    while len(s) > 1:
        if s[0:1] != s[-1:]:
            return False
        s = s[1:len(s)-1]
    return True

largest = 0

for i in xrange(100,1000):
    for j in xrange(100,1000):
        num = i * j
        if palindrome(num):
            if num > largest:
                largest = num

print largest