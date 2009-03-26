memo = {}

def iter_seq(num):
  n = num
  count = 1
  while n != 1:
    #if n in memo.keys():
    #  return count + memo[n] - 1
    if not n % 2:
      n /= 2
    else:
      n = 3*n + 1
    count += 1
  return count


#res = iter_seq(13)
#memo[13] = res
#print res
#print iter_seq(26)
largest = 0
l_num = 0
for x in xrange(1,1000000):
  res = iter_seq(x)
  #memo[x] = res
  if res > largest:
    l_num = x
    largest = res

print l_num
