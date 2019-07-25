# Challenge
# Have the function SimpleAdding(num) add up all the numbers from 1 to num. 
# For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. 
# For the test cases, the parameter num will be any number from 1 to 1000. 

def SimpleAdding(num): 

    finalNumber = 1
    countEqualsNum = False
    count = 1

    while (countEqualsNum == False):
        count+=1
        finalNumber = count+finalNumber

        if count == num:
            countEqualsNum = True

    return finalNumber

number = 12  
print (SimpleAdding(number))

