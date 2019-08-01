# Challenge
# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning 
# the string true or false. 
# The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a) and for the string to be true each 
# letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 

def SimpleSymbols(str): 

    count = 0
    simpleSymbol = "true"
    for letter in str:
        if letter.isalpha():
            if (str[count-1] != "+" or str[count+1] != "+") or count == 0:
                simpleSymbol = "false"
            else:
                break
        count += 1

    return simpleSymbol
    
# keep this function call here  
# print SimpleSymbols(raw_input())

a = "f++d+"
print(SimpleSymbols(a))