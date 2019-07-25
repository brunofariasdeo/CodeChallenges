# Challenge
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
# For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

def FirstReverse(str): 

    count = 1
    reversedString = ""
    while len(str) >= count:
        reversedString += str[-count]
        count+= 1

    return reversedString 
    
# keep this function call here  
a = "Coderbyte"

FirstReverse(a)
