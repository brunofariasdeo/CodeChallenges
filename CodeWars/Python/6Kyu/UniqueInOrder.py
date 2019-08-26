# Link: https://www.codewars.com/kata/unique-in-order/train/python

def unique_in_order(iterable):
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList

print(unique_in_order('AAAABBBCCDAABBB'))