def alphabet_position(text):
    finalString = ""

    for letter in text:
        if letter.isalpha():
            if ord(letter)>=65 and ord(letter)<= 90:
                finalString += str((ord(letter)) - 64) + " "
            elif ord(letter)>=97 and ord(letter)<=122:
                finalString += str((ord(letter)) - 96) + " "

    finalString = finalString[:-1]

    return finalString

print(alphabet_position("The sunset sets at twelve o' clock."))

