# URL: https://www.codewars.com/kata/find-duplicates/train/python

def duplicates(array):
  duplicatesList=[]
  numbersFound = []

  for index, item in enumerate(array):
    if (item in numbersFound) and (item not in duplicatesList):
      duplicatesList.append(item)
    else:
      numbersFound.append(item)
      
  return duplicatesList

print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']))