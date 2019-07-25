# Challenge
# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

def LetterChanges(str): 

    wordString= ""

    for letter in str:
        if ord(letter) == 90 or ord(letter) == 122:
            letter = "A"
            wordString += letter
        else:
            if (ord(letter) >= 65 and ord(letter) <=90) or (ord(letter)>=97 and ord(letter)<=122):

                letter = chr(ord(letter)+1)

                if ord(letter) == 97 or ord(letter) == 101 or ord(letter) == 105 or ord(letter) == 111 or ord(letter) == 117:
                    letter = chr(ord(letter)-32)
                    wordString += letter
                    
                else:
                    wordString += letter
            
            else:
                wordString += letter

    return wordString
    

# stringInput = "hello*3"
stringInput = "a confusing /:sentence:/[ this is not!!!!!!!~"
print (LetterChanges(stringInput))  