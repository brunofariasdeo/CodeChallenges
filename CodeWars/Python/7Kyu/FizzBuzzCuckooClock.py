# Link: https://www.codewars.com/kata/fizz-buzz-cuckoo-clock/train/python

def fizz_buzz_cuckoo_clock(time):
    timeList = list(map(int,time.split(":")))

    if timeList[1] % 3 == 0 and timeList[1] != 0 and timeList[1] != 30:
        if timeList[1] % 5 == 0:
            return "Fizz Buzz"
        else:
            return "Fizz"
    elif timeList[1] % 5 == 0 and timeList[1] != 0 and timeList[1] != 30:
        if timeList[1] % 3 == 0:
            return "Fizz Buzz"
        else:
            return "Buzz"
    elif timeList[1] == 30:
        return "Cuckoo"
    elif timeList[1] == 0:
        if (timeList[0] > 12):
            return str((timeList[0]-12)*("Cuckoo "))[:-1]
        elif (timeList[0] == 0):
            return str(12*("Cuckoo "))[:-1]
        else:
            return str((timeList[0])*("Cuckoo "))[:-1]
    else:
        return "tick"

print(fizz_buzz_cuckoo_clock("00:00"))