# Link: https://www.codewars.com/kata/5878520d52628a092f0002d0

# Given a string, return a new string that has transformed based on the input:

# Change case of every character, ie. lower case to upper case, upper case to lower case.
# Reverse the order of words from the input.
# Note: You will have to handle multiple spaces, and leading/trailing spaces.

# For example:

# "Example Input" ==> "iNPUT eXAMPLE"
# You may assume the input only contain English alphabet and spaces.

def string_transformer(s):
    s = s + " "
    newString = ""
    stringList = []
    for letter in s:
        if letter.islower():
            newString += letter.upper()
        elif letter.isupper():
            newString += letter.lower()
        else:
            newString += letter
            stringList.append(newString)
            newString = ""
 
    stringList.append(newString)
    
    return ''.join(list(reversed(stringList)))[:-1]

print(string_transformer("You Know When  THAT  Hotline Bling"))