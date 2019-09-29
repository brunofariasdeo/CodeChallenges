# Link: https://www.codewars.com/kata/logical-calculator/train/python

def logical_calc(array, op):
    if op == "AND":
        return min(array)
    elif op == "OR":
        return max(array)
    else:
        current = array[0]
        for boolean in array[1:]:
            current = current != boolean

        return current

print(logical_calc([True, False], "OR"))


# from operator import and_, or_, xor

# OPERATOR = {'AND': and_, 'OR': or_, 'XOR': xor}


# def logical_calc(array, op):
#     return reduce(OPERATOR[op], array)