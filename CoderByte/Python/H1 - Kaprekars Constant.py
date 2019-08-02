# Challenge
# Have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at least two distinct digits. 
# Your program should perform the following routine on the number:
# Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number), 
# and subtract the smaller number from the bigger number. 
# Then repeat the previous step. Performing this routine will always cause you to reach a fixed number: 6174. 
# Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174). 
# Your program should return the number of times this routine must be performed until 6174 is reached. 
# For example: if num is 3524 your program should return 3 because of the following steps: 
# (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174. 

def KaprekarsConstant(num): 

    kaprekarsFound = False
    count = 0

    while kaprekarsFound == False:

        count += 1
        stringList = []

        while len(str(num)) < 4: 
            num = '0' + str(num)

        for number in str(num):
            stringList.append(number)

        ascendingOrder = sorted(stringList)
        descendingOrder = sorted(stringList, reverse = True)

        ascendingString = ""
        for number in ascendingOrder:
            ascendingString += number

        descendingString = ""
        for number in descendingOrder:
            descendingString += number

        finalNumber = int(descendingString) - int(ascendingString)

        while len(str(finalNumber)) < 4: 
            finalNumber = '0' + str(finalNumber)
        
        num = int(finalNumber)

        if num == 6174:
            kaprekarsFound = True

    return count
    
# keep this function call here  
a = 9831
print (KaprekarsConstant(a))  