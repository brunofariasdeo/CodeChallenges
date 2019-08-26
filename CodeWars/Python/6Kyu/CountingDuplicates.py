# Link: https://www.codewars.com/kata/counting-duplicates/train/python

from collections import Counter

def duplicate_count(text):
    duplicateDict = Counter(list(text.lower()))
    duplicateCount = 0

    for keys in duplicateDict:
        if duplicateDict[keys] > 1:
            duplicateCount +=1

    return duplicateCount
     
print(duplicate_count("aabBcde"))