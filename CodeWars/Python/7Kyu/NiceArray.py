# Link: https://www.codewars.com/kata/nice-array/train/python

def is_nice(arr):
    if len(arr)>1:
        niceArrayDict = {}
        for number in arr:
            niceArrayDict[number] = 0
            if (number-1 in arr) or (number+1 in arr):
                niceArrayDict[number] = 1

        if 0 in niceArrayDict.values():
            return False
        else:
            return True
    else:
        return False

print(is_nice([3,4,5,7]))