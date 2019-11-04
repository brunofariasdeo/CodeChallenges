# Link: https://www.codewars.com/kata/ordered-count-of-characters/train/python
from collections import OrderedDict 

def ordered_count(input):
  lettersDict = OrderedDict()
  tupleList = []

  for letter in input:
    if letter in lettersDict.keys():
      lettersDict[letter]+=1
    else:
      lettersDict[letter]=1
  
  for letter in lettersDict.keys():
    tupleList.append((letter,lettersDict[letter]))

  return tupleList

print(ordered_count('abracadabra'))