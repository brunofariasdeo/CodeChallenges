# URL: https://www.codewars.com/kata/simple-remove-duplicates/train/python

def solve(arr): 
  numbersFound = []

  arr = list(reversed(arr))

  for index, item in enumerate(arr):
    if (item not in numbersFound):
      numbersFound.append(item)
      
  return list(reversed(numbersFound))

print(solve([1,2,1,2,1,2,3]))

