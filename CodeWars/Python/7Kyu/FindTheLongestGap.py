# URL: https://www.codewars.com/kata/find-the-longest-gap/train/python

def gap(num):
  maxLengthFound = 0
  stringLoop = ""

  binary = bin(num)[2:];

  for number in binary:
    if (number == "1"):
      if (maxLengthFound<len(stringLoop)):
        maxLengthFound = len(stringLoop)
      stringLoop = ""
    else:
      stringLoop += number 

  return maxLengthFound

print(gap(15))