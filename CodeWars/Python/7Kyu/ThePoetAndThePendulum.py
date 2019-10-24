# Link: https://www.codewars.com/kata/the-poet-and-the-pendulum/train/python

def pendulum(values):
    values = sorted(values)

    tempString = ""

    for index, number in enumerate(values):
        if index%2 == 0:
            tempString = str(number) + "," + tempString
        else:
            tempString = tempString + str(number) + ","
            
    return list(map(int, tempString[:-1].split(",")))

print(pendulum([4,6,8,7,5]))

# [8,6,4,5,7]