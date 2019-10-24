# Link: https://www.codewars.com/kata/alternate-capitalization/train/python

def capitalize(s):
    firstString = ""
    secondString = ""

    for index, item in enumerate(s):
        if index % 2 == 0:
            firstString += item.upper()
            secondString += item.lower()
        else:
            firstString += item.lower()
            secondString += item.upper()
        
    return [firstString,secondString]

print(capitalize("abcdef"))