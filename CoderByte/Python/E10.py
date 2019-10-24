def AlphabetSoup(str): 

    orderedList = []

    for letter in str:
        orderedList.append(letter)

    orderedList.sort()

    orderedString = ""
    for letter in orderedList:
        orderedString += letter

    return orderedString
    
# keep this function call here  

a = "antes"
print (AlphabetSoup(a))