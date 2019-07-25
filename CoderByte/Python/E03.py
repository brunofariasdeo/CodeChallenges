# Challenge
# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty. 

def LongestWord(sen): 

    wordsList= []
    wordString= ""

    for word in sen:
        if ord(word) == 32:
            wordsList.append(wordString)
            wordString = ""
        elif (ord(word) >= 65 and ord(word) <=91) or (ord(word)>=97 and ord(word)<=122):
	        wordString += word

    wordsList.append(wordString)

    biggerWord = ""
    for word in wordsList:
        if len(word) > len(biggerWord):
            biggerWord = word

    sen = biggerWord

    return sen
    
# keep this function call here  
a = "dale! meu. pirraia?!.;;-="
print(LongestWord(a))
