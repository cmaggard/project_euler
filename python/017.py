import sys

ones = ["","one","two","three","four","five","six","seven",
         "eight","nine"]
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
ten_mults = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
             "seventy", "eighty", "ninety"]

def to_words(num):
  """
  >>> to_words(1000)
  'Onethousand'
  >>> to_words(999)
  'Ninehundredandninetynine'
  >>> to_words(547)
  'Fivehundredandfortyseven'
  >>> to_words(317)
  'Threehundredandseventeen'
  >>> to_words(96)
  'Ninetysix'
  >>> to_words(5)
  'Five'
  >>> to_words(100)
  'Onehundred'
  """

  res = ""
  if num >= 100:
    if num == 1000:
      return "Onethousand"
    else:
      res += ones[num / 100] + "hundred"
  lower_part = num % 100
  if lower_part and res:
    res += "and"
  if lower_part:
    if lower_part < 10:
      res += ones[lower_part]
    elif lower_part < 20:
      res += tens[lower_part - 10]
    else:
      res += ten_mults[lower_part / 10]
      if lower_part % 10:
        res += ones[lower_part % 10]


  return res.capitalize()


if __name__ == "__main__":
  if 'test' in sys.argv:
    import doctest
    doctest.testmod()
    print len(to_words(342))
    print len(to_words(115))
  else:
    print reduce(lambda x, y: x+y, 
                 [len(to_words(x+1)) for x in xrange(1000)])

