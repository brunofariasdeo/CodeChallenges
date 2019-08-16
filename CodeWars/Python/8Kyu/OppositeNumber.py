# Very simple, given a number, find its opposite.
# Examples:
# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    if number>0:
        newNumber = "-"+str(number)
    elif number<0:
        newNumber = str(number)[1:]
    else:
        newNumber = 0
    print(newNumber)

    return float(newNumber)
  # your solution here

opposite(-3.1458)