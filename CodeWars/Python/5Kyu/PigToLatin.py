# Link: https://www.codewars.com/kata/simple-pig-latin/train/python

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    pigString = ""
    for word in text.split():
        if word.isalpha():
	        pigString += word[1:] + word[0] + "ay" + " "
        else:
            pigString += word
    
    if pigString[-1] == " ":
        return pigString[:-1]
    else:
        return pigString