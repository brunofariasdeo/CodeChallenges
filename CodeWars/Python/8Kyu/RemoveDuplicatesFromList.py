# URL: https://www.codewars.com/kata/remove-duplicates-from-list/train/python

from collections import OrderedDict

def distinct(seq):
  return list(OrderedDict.fromkeys(seq))

print(distinct([1,2,4,3,5,2,3]))