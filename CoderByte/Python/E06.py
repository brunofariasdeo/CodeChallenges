# Challenge
# Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. 
# Words will be separated by only one space. 

def LetterCapitalize(str): 

    stringWord = str.split()
    count = 0
    
    for word in stringWord:
        
        listLetter = []
        for letter in word:
            listLetter.append(letter)

        listLetter[0] = listLetter[0].upper()
        stringWord[count] = ''.join(listLetter)

        count += 1

    stringWord = ' '.join(stringWord)
        
    return stringWord
    
# keep this function call here  
a = "hello world"
print(LetterCapitalize(a)) 