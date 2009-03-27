day = 1
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0

for year in xrange(1900, 2001):
  for month in months:
    day %= 7
    if day == 0 and year != 1900:
      count += 1
    day += month
    if month == 28 and not year % 4:
      # Process leap year
      day += 1

print count
