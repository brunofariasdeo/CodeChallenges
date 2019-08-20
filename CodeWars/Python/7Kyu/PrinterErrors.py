# Link: https://www.codewars.com/kata/printer-errors/train/python

def printer_error(s):
    permitted = "abcdefghijklm"
    notOk = 0

    for letter in s:
        if letter not in permitted:
            notOk +=1            

    return str(notOk) + '/' + str(len(s))